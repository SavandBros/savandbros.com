from typing import Tuple

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from modeltranslation.admin import (
    TabbedDjangoJqueryTranslationAdmin,
    TabbedTranslationAdmin,
    TranslationStackedInline,
)

from planet.forms import SectionItemModelForm
from planet.models import (
    MoneyCurrency,
    Price,
    ProductGroup,
    Product,
    Section,
    SectionItem,
)


class ProductPriceInline(admin.TabularInline):
    """Price Inline."""
    model = Price
    max_num = 7


@admin.register(MoneyCurrency)
class MoneyCurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'rate', )
    search_fields = ('code', )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('pricing_type', 'price', )
    list_filter = ('pricing_type', )


@admin.register(ProductGroup)
class ProductGroupAdmin(TabbedDjangoJqueryTranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', 'description', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(TabbedDjangoJqueryTranslationAdmin):
    list_display = ('name', 'slug', 'featured', 'in_stock', )
    list_filter = ('featured', 'in_stock', )
    search_fields = ('name', 'description', )
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ProductPriceInline, ]


class SectionItemInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = SectionItem
    form = SectionItemModelForm


@admin.register(Section)
class SectionAdmin(TabbedDjangoJqueryTranslationAdmin):
    list_display: Tuple[str] = ('name', )
    search_fields: Tuple[str] = ('name', 'description', )


@admin.register(SectionItem)
class SectionItemAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    list_display: Tuple[str] = ('section', 'title', 'icon', )
    search_fields: Tuple[str] = ('title', 'description', )
    form = SectionItemModelForm
