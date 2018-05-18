from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display_links = (
        'location', # location을 클릭함으로 이미지편집을 할 수 있다.
        'caption',
    )

    search_fields = (
        'location', # location으로 검색할 수 있는 검색바 생성.
        'caption',
    )

    list_filter = (
        'location', # location으로 된 filter를 오른쪽에 생성.
        'creator',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )