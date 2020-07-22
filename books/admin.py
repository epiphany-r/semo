from django.contrib import admin

from .models import BookCategory, Book, Publisher

admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Publisher)