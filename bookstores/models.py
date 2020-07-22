from django.db import models


class Bookstore(models.Model):
    bookstoreName = models.CharField(verbose_name="서점 이름", max_length=20)
    bookstoreExp = models.TextField(verbose_name="서점 정보")
    bookstoreAddress = models.CharField(verbose_name="서점 주소", max_length=200)
    bookstoreTel = models.CharField(verbose_name="서점 연락처", blank=True, max_length=30)
    bookstorePic = models.ImageField(
        verbose_name="서점 이미지", upload_to="bookstore/%Y/%m/%d", blank=True
    )

    def __str__(self):
        return self.bookstoreName

