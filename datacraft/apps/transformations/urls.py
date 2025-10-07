from django.urls import path, include

from . import views

app_name = 'transformations'

urlpatterns = [
    path("", views.index, name="index")
]