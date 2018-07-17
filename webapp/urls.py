from __future__ import unicode_literals
from django.db import migrations
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




urlpatterns = [
    # /course/Chapter/Class/Chapter
    # /course/matrices/12/mathematics
    #(?P<Chapter>[a-zA-Z0-9_.-]+)
    url(r'^$', views.courseList.as_view()),
    url(r'^completion$', views.completion, name = 'completion'),
    
]
