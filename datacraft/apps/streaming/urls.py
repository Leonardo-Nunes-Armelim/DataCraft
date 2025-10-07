from django.urls import path, include

from . import views

app_name = 'streaming'

urlpatterns = [
    path("", views.index, name="index")
]