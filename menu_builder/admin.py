from typing import Tuple, List

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from menu_builder.forms import NavigationLinkModelFormNoTrans
from menu_builder.models import Menu, NavigationLink


class NavigationLinkInline(SortableInlineAdminMixin, admin.TabularInline):
    """Navigation Link model Inline."""
    model = NavigationLink
    form = NavigationLinkModelFormNoTrans


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Menu model admin."""
    list_display: Tuple[str] = ('name', )
    inlines: List[admin.TabularInline] = [
        NavigationLinkInline,
    ]


@admin.register(NavigationLink)
class NavigationLinkAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    """Navigation Link model admin."""
    list_display: Tuple[str] = (
        'menu',
        'label',
        'external_link',
        'internal_link',
        'icon',
        'open_in_new_tab',
        'parent',
    )
    search_fields: Tuple[str] = ('label', 'external_link', )
