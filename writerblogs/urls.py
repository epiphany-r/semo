from django.urls import path
from writerblogs.views import WriterBlogListView,WriterBlogDetail,WriterBlogCreateView,WriterBlogUpdateView,WriterBlog_delete

app_name = "writerblogs"

urlpatterns = [
    path("", WriterBlogListView.as_view(), name="writerblog"),
    path("<int:pk>/",WriterBlogDetail.as_view(),name ="detail"),
    path("create/",WriterBlogCreateView.as_view(),name="create"),
    path("<int:pk>/update/",WriterBlogUpdateView.as_view(),name="update"),
    path("<int:pk>/delete/",WriterBlog_delete,name= "delete"),
]
