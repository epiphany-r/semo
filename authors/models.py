from django.db import models

# Create your models here.
class Author(models.Model):

    authorName = models.CharField(max_length=50, verbose_name="저자이름")
    authorExp = models.TextField(blank=True, verbose_name="저자설명")
    authorEmail = models.EmailField(blank=True, max_length=30, verbose_name="저자이메일")

    def __str__(self):
        return self.authorName
