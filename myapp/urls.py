from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', 
         views.IndexView.as_view(), 
         name='index'),

    path('post/', 
         views.CreateCompanyView.as_view(), 
         name='post'),

    path('list/', 
         views.PostView.as_view(), 
         name='list'),

    path('success/',
         views.PostSuccessView.as_view(),
         name = 'success'),

     path('todo/', 
          views.TodoListView.as_view(), 
          name='todo_list'),

    path('todo/toggle/<int:task_id>/', 
         views.toggle_task, 
         name='toggle_task'),

    path('todo/delete/<int:task_id>/', 
         views.delete_task, 
         name='delete_task'),  

    path('detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'detail'),
    
    path('search/', 
         views.CompanyListView.as_view(), 
         name='search'),

     path('contact/',
          views.ContactView.as_view(),
          name='contact')
]


