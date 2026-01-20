# Glory be to LORD our GOD

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]