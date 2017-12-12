from typing import Tuple

from cms.forms.fields import PageSelectFormField
from django import forms

from planet import conf
from planet.models import SectionPlugin, SectionItem


class SectionPluginPublisherForm(forms.ModelForm):
    """
    Section Plugin Publisher Form.

    Override template field choices in the form, instead of having choices
    defined in the model field directly.

    The issue with defining choices in the model field is, whenever a new
    template is added to :attr:``conf.SECTION_TEMPLATES`` we need to
    generate new migrations for the model and migrate the database.
    """
    class Meta:
        model = SectionPlugin
        fields = ('section', 'template', )

    template = forms.ChoiceField(choices=conf.SECTION_TEMPLATES)


class SectionItemModelForm(forms.ModelForm):
    """Section Item Model Form."""
    class Meta:
        model = SectionItem
        exclude: Tuple[str] = ()

    internal_link = PageSelectFormField(required=False)
