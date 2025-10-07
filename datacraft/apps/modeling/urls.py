from django.urls import path, include

from . import views

app_name = 'modeling'

urlpatterns = [
    path("", views.index, name="index")
]