from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("author/", views.ThisMonthAuthorListView.as_view(), name="author"),
    path("book/", views.ThisMonthBookView, name="book"),
    path("event/", views.ThisMonthEventView, name="event"),
    path("result/", views.result, name="result"),
]
