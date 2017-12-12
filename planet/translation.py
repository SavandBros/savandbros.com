from typing import Tuple

from modeltranslation.translator import translator, TranslationOptions

from planet.models import (
    Product,
    ProductGroup,
    Team,
    TeamMember,
    Section,
    SectionItem,
)


class ProductTranslationOptions(TranslationOptions):
    fields = ('slug', 'name', 'description', 'info', 'label', 'order_link', )


class ProductGroupTranslationOptions(TranslationOptions):
    fields = ('slug', 'name', 'description', )


class TeamTranslationOptions(TranslationOptions):
    fields = ('name', )


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'bio', )


class SectionTranslationOptions(TranslationOptions):
    fields: Tuple[str] = ('title', 'sub_title', 'description', )


class SectionItemTranslationOptions(TranslationOptions):
    fields: Tuple[str] = ('title', 'description', 'external_link', )


translator.register(Product, ProductTranslationOptions)
translator.register(ProductGroup, ProductGroupTranslationOptions)
translator.register(Team, TeamTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(SectionItem, SectionItemTranslationOptions)
