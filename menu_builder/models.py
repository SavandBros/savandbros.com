from typing import Union

from cms.models import Page, CMSPlugin
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _


class Menu(models.Model):
    """Menu model."""
    name = models.CharField(verbose_name=_('name'), max_length=100)

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')

    def __str__(self) -> str:
        return self.name

    @property
    def ancestors(self) -> QuerySet:
        return NavigationLink.objects.parents(menu=self)


class NavigationLinkManager(models.Manager):
    """Navigation Link Manager."""
    def parents(self, menu: Menu) -> QuerySet:
        return self.filter(parent=None, menu=menu)


class NavigationLink(models.Model):
    """Navigation Link model."""
    menu = models.ForeignKey(Menu, related_name='links')

    label = models.CharField(
        verbose_name=_('label'),
        blank=True,
        null=True,
        max_length=100,
    )
    external_link = models.URLField(
        verbose_name=_('external link'),
        blank=True,
        null=True
    )
    internal_link = models.ForeignKey(
        Page,
        verbose_name=_('internal link'),
        blank=True,
        null=True,
    )
    icon = models.CharField(
        verbose_name=_('icon'),
        help_text=_(
            'an Icon from our icon/font framework, for instance "fa fa-login"'
        ),
        max_length=25,
        blank=True,
        null=True,
    )
    open_in_new_tab = models.BooleanField(
        verbose_name=_('open in new tab'),
        default=False,
    )
    link_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )

    objects = NavigationLinkManager()

    class Meta:
        verbose_name = _('Navigation Link')
        verbose_name_plural = _('Navigation Links')
        ordering = ('link_order', )

    def __str__(self) -> str:
        return self.label

    @property
    def link(self) -> Union[str, None]:
        """Get the link form the internal_link or the internal_link(Page)."""
        link = None

        if self.internal_link:
            link = self.internal_link.get_absolute_url()

        if self.external_link:
            link = self.external_link

        return link


class MenuPlugin(CMSPlugin):
    """Menu model CMS Plugin."""
    menu = models.ForeignKey(Menu)

    def __str__(self) -> str:
        return self.menu.name
