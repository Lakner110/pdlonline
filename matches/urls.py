from django.urls import path

from . import views

urlpatterns = [ 
    path("replay_analyzer/", views.replay_analyzer, name="replay_analyzer"),
    path("replay_analyzer/html/", views.replay_analyzer_html, name="replay_analyzer_html"),
]