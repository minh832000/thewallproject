from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('employer/', views.recruiterHome, name='r-home'),
]