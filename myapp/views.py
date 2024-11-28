from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.urls import reverse_lazy
from .forms import CompanyForm
from .models import Task
from .forms import TaskForm, ContactForm
from django.utils.decorators import method_decorator
from .models import Company
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic.edit import FormMixin
from django.db.models import Q

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Company.objects.order_by('-name')
    paginate_by = 8

class PostView(ListView):
    template_name = "list.html"
    queryset = Company.objects.order_by('-name')

class CreateCompanyView(CreateView):
    form_class = CompanyForm
    template_name = "post.html"
    success_url = reverse_lazy('myapp:success')

    def form_valid(self, form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user

        if not postdate.strengths:
            postdate.strengths = "特になし"
        if not postdate.location:
            postdate.location = "未定"
        if not postdate.working_hours:
            postdate.working_hours = "不明"
        if not postdate.salary:
            postdate.salary = "要相談"
        if not postdate.benefits:
            postdate.benefits = "特になし"
        if not postdate.annual_holidays:
            postdate.annual_holidays = "未定"
        if not postdate.hires:
            postdate.hires = "不明"
        if not postdate.selection_process:
            postdate.selection_process = "選考フローは未定"
        if not postdate.notes:
            postdate.notes = "特記事項なし"

        postdate.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'success.html'

class TodoListView(FormMixin, ListView):
    model = Task
    template_name = 'todo.html'
    context_object_name = 'tasks'
    form_class = TaskForm

    def get_queryset(self):
        return Task.objects.all().order_by('-id')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect('myapp:todo_list')
        return self.form_invalid(form)


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('myapp:todo_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('myapp:todo_list')

class DetailView(DetailView):
    model = Company
    template_name = 'detail.html'


class CompanyListView(ListView):
    model = Company
    template_name = 'search.html'
    context_object_name = 'companies'

    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()
        sort = self.request.GET.get('sort', '').strip()

        queryset = Company.objects.all()

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)  
            )

        valid_sort_fields = ['name', '-name', 'created_at', '-created_at']  
        if sort in valid_sort_fields:
            queryset = queryset.order_by(sort)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '').strip()
        context['sort'] = self.request.GET.get('sort', '').strip()
        return context


class ContactView(FormView):

    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('myapp:contact')

    def form_valid(self, form):
    
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        
        message = \
          '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
          .format(name, email, title, message)
        from_email = 'ngn2449954@stu.o-hara.ac.jp'
        to_list = ['ngn2449954@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(
          self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)