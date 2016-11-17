from django.db import models

# page extension imports
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

# django filer imports
from filer.fields.image import FilerImageField


class PageFieldExtension(PageExtension):
    subtitle = models.CharField(max_length=255, blank=True)
    background_image = FilerImageField(blank=True)

extension_pool.register(PageFieldExtension)
