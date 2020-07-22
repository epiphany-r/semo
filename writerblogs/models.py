from django.db import models
from users import models as user_models


class WriterBlog(models.Model):

    postTitle = models.CharField(max_length=30, verbose_name="포스트제목")
    postExp = models.TextField(verbose_name="포스트내용")
    postDate = models.DateField(auto_now_add=True, verbose_name="포스트등록날짜")
    postPic = models.ImageField(
        upload_to="writerblogs/postPic", verbose_name="포스트사진", blank=True, null=True
    )
    userID = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.postTitle
