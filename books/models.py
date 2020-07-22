from django.db import models
from authors import models as author_models


class BookCategory(models.Model):
    bookCategory = models.CharField(verbose_name="카테고리이름", max_length=200)

    def __str__(self):
        return self.bookCategory


class Publisher(models.Model):
    publisherName = models.CharField(verbose_name="출판사이름", max_length=200)
    publisherAddress = models.CharField(verbose_name="출판사주소", max_length=200)
    publisherWeb = models.URLField(verbose_name="출판사홈페이지", max_length=200)

    def __str__(self):
        return self.publisherName


class Book(models.Model):
    bookCategoryID = models.ForeignKey(
        BookCategory, verbose_name="도서카테고리ID", on_delete=models.CASCADE, blank=True
    )
    bookTitle = models.CharField(verbose_name="도서제목", max_length=200)
    authorID = models.ForeignKey(
        author_models.Author, verbose_name="저자ID", on_delete=models.CASCADE, blank=True
    )
    publisherID = models.ForeignKey(
        Publisher, verbose_name="출판사ID", on_delete=models.CASCADE, blank=True
    )
    price = models.PositiveIntegerField(verbose_name="가격")
    bookExp = models.TextField(verbose_name="도서설명", null=True, blank=True)
    bookPic = models.ImageField(
        verbose_name="도서사진", upload_to="books/%Y/%m/%d", blank=True
    )
    publisherDate = models.DateField(verbose_name="출판일")

    def __str__(self):
        return self.bookTitle
