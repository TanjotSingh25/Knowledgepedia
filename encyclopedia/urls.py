from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_new_page", views.add_new_page, name="add_new_page"),
    path("random", views.random, name="random"),
    path("edit/<str:topic>", views.edit_page, name="edit_page"),
    path("search_results", views.search_results, name="search"),
    path("<str:topic>", views.render_page, name="render_page")
]
