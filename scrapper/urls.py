from django.urls import path
from .views import get_stories

urlpatterns=[path("getTimesStories/",get_stories, name="get-latest-stories")]