from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiList, name="api-listOverview"),
]
