from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<title>", views.display_entry, name="entry"),
    path("new/", views.new_entry, name="new"),
]