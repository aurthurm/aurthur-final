from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

class PortfolioAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Content'), {
            'fields': (('title', 'slug'), 'content',)}),
        (_('Illustration'), {
            'fields': ('image', 'image_caption',)}),
        (_('Links'), {
            'fields': ('github_link',)}),
        (_('Publication'), {
            'fields': ('creation_date',)
            }
        )
	)

admin.site.register(Portfolio, PortfolioAdmin)