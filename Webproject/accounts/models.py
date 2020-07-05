from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    userID = models.CharField(verbose_name='회원ID', max_length=20)
    userPW = models.CharField(verbose_name='회원비밀번호', max_length=20)
    nickName = models.CharField(verbose_name='닉네임', max_length=20)
    userEmail = models.EmailField(verbose_name='이메일', max_length=200)
    userAddress = models.CharField(verbose_name='주소', max_length=200)
    userTel = models.IntegerField(verbose_name='전화번호', max_length=20)
    writerIntro = models.TextField(verbose_name='작가소개', null=True, blank=True)
    userPic = models.ImageField(verbose_name='회원사진', upload_to='images', null=True, blank=True)
    userGrade = models.BooleanField(verbose_name='회원등급', default=False)

class likebook(models.Model):
    userID = models.ForeignKey('Users', on_delete=models.CASCADE)
    bookCategoryID = models.CharField(verbose_name='도서카테고리ID', max_length=20)

    def __str__(self):
        return self.bookCategoryID
    
