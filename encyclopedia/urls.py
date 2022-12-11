from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<title>", views.display_entry, name="entry"),
    path("new/", views.new_entry, name="new"),
    path("<title>/edit", views.new_entry, name="edit"),
    path("search/", views.search_entry, name="search")
]