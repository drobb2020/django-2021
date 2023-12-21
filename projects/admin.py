# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Project, Review, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'title',
        'description',
        'featured_image',
        'live_link',
        'code_link',
        'vote_total',
        'vote_ratio',
    )
    list_filter = ('owner', 'created_at', 'updated_at')
    raw_id_fields = ('tags',)
    date_hierarchy = 'created_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'project',
        'body',
        'value',
    )
    list_filter = ('owner', 'project', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'id')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
