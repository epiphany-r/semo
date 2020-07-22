from django.urls import path
from . import views

app_name='bookstores'

urlpatterns = [
    path('', views.BookstoreListView.as_view(), name='list'),
    path('<int:pk>/detail', views.BookstoreDetailView.as_view(), name='detail'),
    path('create', views.BookstoreCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.BookstoreUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.bookstore_delete, name='delete'),
    path('search/', views.BookstoreSearchView.as_view(), name='search'),
]