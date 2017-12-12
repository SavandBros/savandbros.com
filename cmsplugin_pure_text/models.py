from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PureText(CMSPlugin):
    """Text Model."""
    content = models.TextField(verbose_name=_('content'))

    def __str__(self):
        return self.content
