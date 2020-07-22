import os
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # ID = models.CharField(verbose_name="회원ID", max_length=20, primary_key=True)
    # userPW = models.CharField(verbose_name="회원비밀번호", max_length=20)
    nickName = models.CharField(verbose_name="닉네임", max_length=20)
    userEmail = models.EmailField(verbose_name="이메일", max_length=200)
    userAddress = models.CharField(verbose_name="주소", max_length=200)
    userTel = models.CharField(verbose_name="전화번호", max_length=20)
    writerIntro = models.TextField(verbose_name="작가소개", null=True, blank=True)
    userGrade = models.BooleanField(verbose_name="회원등급", default=False)
    userPic = models.ImageField(
        verbose_name="회원사진", blank=True, upload_to="userpic/%Y/%m/%d"
    )

    def __str__(self):
        return self.username

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.userPic.path))
        super(User, self).delete(*args, **kargs)


class likebook(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bookCategoryID = models.CharField(verbose_name="관심장르", max_length=20, null=True)
