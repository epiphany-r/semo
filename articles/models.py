from django.db import models
from users import models as user_models
from books import models as book_models
from authors import models as author_models


class Article(models.Model):

    article_choices = [
        ("book", "도서"),
        ("event", "행사"),
        ("author", "저자"),
    ]

    # <필수항목>
    articleCategory = models.CharField(
        verbose_name="기사카테고리", choices=article_choices, max_length=255
    )  # 기사카테고리
    articleTitle = models.CharField(verbose_name="기사제목", max_length=255)  # 기사제목
    articleExp = models.TextField(verbose_name="기사내용")  # 기사 내용
    articleDate = models.DateField(verbose_name="기사등록날짜", auto_now_add=True)  # 기사등록날짜

    # <선택항목>
    eventName = models.CharField(verbose_name="행사이름", max_length=255, null=True)  # 행사이름
    bookID = models.ForeignKey(
        book_models.Book,
        verbose_name="도서ID",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )  # 도서ID
    userID = models.ForeignKey(
        user_models.User,
        verbose_name="회원ID",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )  # 회원ID
    authorID = models.ForeignKey(
        author_models.Author,
        verbose_name="저자ID",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )  # 저자ID
    bookArticlePic = models.ImageField(
        verbose_name="도서기사사진", upload_to="articles/book/", null=True, blank=True
    )  # 도서기사사진
    eventArticlePic = models.ImageField(
        verbose_name="행사기사사진", upload_to="articles/event/", null=True, blank=True
    )  # 행사기사사진
    authorArticlePic = models.ImageField(
        verbose_name="저자기사사진", upload_to="articles/author/", null=True, blank=True
    )  # 저자기사사진

    def __str__(self):
        return self.articleTitle
