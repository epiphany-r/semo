from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.WriterBlog)
class WriterBlogAdmin(admin.ModelAdmin):

    list_display = ("postTitle", "postExp", "postDate", "postPic", "userID")

    search_fields = [
        "postTitle",
    ]

    fieldsets = (("게시글정보", {"fields": ("postTitle", "postExp", "postPic", "userID"),}),)

    # def get_thumbnail(self, obj):
    #     return mark_safe(f'<img src="{obj.postPic.url}"/>')

    # get_thumbnail.short_description = "포스트사진"
