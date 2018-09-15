from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

class ServicesEntryAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Services'), {
            'fields': ('title', 'content',)}),
	)

class SubjectAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Subject'), {
            'fields': ('title',)}),
	)

class TeachingEntryAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Teaching'), {
            'fields': ('subject', 'title', 'content', 'tag', 'category')}),
	)

class TechToolsAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Technologies'), {
            'fields': ('title', 'image',)}),
	)

class HomePageHeadingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Home Page Headings'), {
            'fields': ('services_title', 'teaching_title', 'technologies_title',)}),
	)

admin.site.register(ServicesEntry, ServicesEntryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TeachingEntry, TeachingEntryAdmin)
admin.site.register(TechTools, TechToolsAdmin)
admin.site.register(HomePageHeadings, HomePageHeadingsAdmin)

