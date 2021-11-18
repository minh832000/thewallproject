from django.urls import path
from . import views

urlpatterns = [
      path('listjob/', views.listJob, name='list-job'),
      path('listjob/search-post/', views.search_post, name='search-post'),
      path('listjob/search/', views.search, name='search-form'),
      path('listjob/filter/', views.filter, name='filter'),
      path('detail/<int:post_id>', views.detailJob, name='detail-job'),
      path('add-post/', views.addNewPost, name='add-new-post'),
      path('edit-post/<int:post_id>', views.editPost, name='edit-post'),
      path('save-edit/<int:post_id>', views.saveEdit, name='save-edit'),
      path('add-post/search/', views.search_result, name='search'),
      path('add-post/add-skill/', views.add_skill, name='add-skill'),
      path('save/', views.savePost, name='save'),
]