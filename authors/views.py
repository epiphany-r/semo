from django.shortcuts import render
from authors.models import Author
from writerblogs.models import WriterBlog
from users.models import User
# Create your views here.


def author(request, pk):
    pk_authors = Author.objects.get(pk=pk)
    all_authors = Author.objects.all()
    all_writerblogs = WriterBlog.objects.all()
    all_userpics = User.objects.all()
    return render(request, "authors/authors.html", context={"authors": pk_authors, "writerblogs":all_writerblogs, "userpics":all_userpics})


