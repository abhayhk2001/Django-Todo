from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiList, name="api-listOverview"),
    path('all-tasks/', views.taskList, name="All-Tasks"),
    path('context/', views.contextList, name="All-Contexts"),
    path('task/<int:pk>/', views.viewTask, name="View-Task"),
    path('add-task/', views.addTask, name="Add Task"),
    path('update-task/<int:pk>/', views.updateTask, name="Update Task"),
    path('delete-task/<int:pk>/', views.deleteTask, name="Delete Task")
]
