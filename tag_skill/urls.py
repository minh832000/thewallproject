from django.urls import path

from .views import SkillTag

urlpatterns = [
      path('skill/', SkillTag.as_view(), name='search_skill_tag'),
]