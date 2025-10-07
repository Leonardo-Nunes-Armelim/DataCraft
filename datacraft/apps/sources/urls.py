from django.urls import path, include

from . import views

app_name = 'sources'

urlpatterns = [
    path("", views.index, name="index")
]