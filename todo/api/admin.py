from django.contrib import admin
from .models import Task, Context
# Register your models here.

admin.site.register(Task,)
admin.site.register(Context)
