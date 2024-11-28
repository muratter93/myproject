from django.contrib import admin

# Register your models here.

from .models import Company, Task

admin.site.register(Company)

admin.site.register(Task)