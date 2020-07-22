from django.shortcuts import render
from books.models import Book
from articles.models import Article

# 홈 html 뷰입니다.


def home(request):
    recent_books = Book.objects.order_by("-pk")[:4]  # 최신 책 4개
    writers_books = Book.objects.all()[:4]  # 작가의 책 4개 (임의로 오래된 책 4개)
    special_article = Article.objects.filter(articleCategory="book").order_by("-pk")[
        :1
    ]  # 기획전 이달의도서 최신 1개

    return render(
        request,
        "home/home.html",
        context={
            "books": recent_books,
            "writers_books": writers_books,
            "special_article": special_article,
        },
    )
