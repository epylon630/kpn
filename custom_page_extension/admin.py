from django.contrib import admin

# page extension imports
from cms.extensions import PageExtensionAdmin

# import our model from ``models.py``
from .models import PageFieldExtension


class PageFieldExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(PageFieldExtension, PageFieldExtensionAdmin)
