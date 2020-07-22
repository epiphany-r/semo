from django.urls import path
from books import views

app_name = "books"

urlpatterns = [
    # books/
    path("", views.BookList.as_view(), name="list"),
    # books/search/
    path("search/", views.BookSearchView.as_view(), name="search"),
    # books/도서ID/
    path("<int:pk>/", views.BookDetailView.as_view(), name="detail"),
]
