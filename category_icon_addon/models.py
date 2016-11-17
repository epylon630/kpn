from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

@python_2_unicode_compatible
class Category(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label

@python_2_unicode_compatible
class Icon(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CategoryIcon(CMSPlugin):
    icon = models.ForeignKey(Icon)
    icon_image = FilerImageField(blank=True)
    url = models.CharField(('link'), max_length=255, blank=True, null=True, help_text='If present, clicking on image will take user to link.')
    link_title = models.CharField(
        blank=True,
        max_length=200,
    )
    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.link_title or self.url_link

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey (icon), it's required to copy over
        # the reference to the Icon instance to the new plugin.
        self.icon = oldinstance.icon