from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<str:title>", views.page, name = "page"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name = "newpage"),
    path("editpage", views.editpage, name="editpage")
]