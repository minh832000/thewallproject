from django.urls import path
from . import views

urlpatterns = [
      path('listjob/', views.listJob, name='list-job'),
      path('detail/', views.detailJob, name='detail-job'),
      path('add-post/', views.addNewPost, name='add-new-post'),
      path('save/', views.savePost, name='save'),
]