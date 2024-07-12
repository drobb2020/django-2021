# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Profile, Skill, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'username',
        'location',
        'short_intro',
        'created_at',
    )
    list_filter = ('user', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'name',
        'description',
    )
    list_filter = ('owner', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'recipient',
        'name',
        'email',
        'subject',
        'is_read',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'sender',
        'recipient',
        'is_read',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
