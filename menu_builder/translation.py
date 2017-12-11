from modeltranslation.translator import translator, TranslationOptions

from menu_builder.models import NavigationLink


class NavigationLinkTranslationOptions(TranslationOptions):
    fields = ('label', )


translator.register(NavigationLink, NavigationLinkTranslationOptions)
