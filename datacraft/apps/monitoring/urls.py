from django.urls import path, include

from . import views

app_name = 'monitoring'

urlpatterns = [
    path("", views.index, name="index")
]