from django.forms import ModelForm
from .models import Company,Task
from django import forms
from django.core.mail import send_mail
from django.core.mail import BadHeaderError

class CompanyForm(ModelForm):

    class Meta:

        model = Company
        fields = ['name', 'image', 'job_description', 'strengths', 'location', 'working_hours', 'salary', 'benefits', 'annual_holidays', 'hires', 'selection_process', 'notes'] 


class TaskForm(ModelForm):

    class Meta:

        model = Task
        fields = ['title']



class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.CharField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
        'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = \
        'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = \
        'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = \
        'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'

