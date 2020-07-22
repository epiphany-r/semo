from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ('authorName', 'authorExp', 'authorEmail')
    list_filter = ('authorName',)
    search_fields = ['authorName', 'authorEmail']

    fieldsets = (
        ("저자정보", {
            "fields": ('authorName', 'authorExp', 'authorEmail'
                
            ),
        }),
    )
    