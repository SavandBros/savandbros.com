from typing import Union

from cms.models import CMSPlugin, Page
from colorfield.fields import ColorField
from currencies import Currency
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from planet import conf


class MoneyCurrency(models.Model):
    """Money Currency."""
    code = models.CharField(
        verbose_name=_("code"),
        max_length=3,
        unique=True,
        choices=((k, k) for k in Currency.get_currency_formats())
    )
    rate = models.DecimalField(
        verbose_name=_('rate'),
        decimal_places=6,
        max_digits=25,
    )

    class Meta:
        verbose_name = _('Money Currency')
        verbose_name_plural = _('Money Currencies')

    def get_currency_parser(self):
        """Return Money Currency parser."""
        return Currency(self.code)

    def __str__(self):
        return self.code


class ProductGroup(models.Model):
    """Product Group model."""
    name = models.CharField(verbose_name=_('name'), max_length=50)
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    description = HTMLField(verbose_name='description')

    class Meta:
        verbose_name = _('Product Group')
        verbose_name_plural = _('Product Groups')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model."""
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    name = models.CharField(verbose_name=_('name'), max_length=50)
    description = HTMLField(verbose_name='description')
    featured = models.BooleanField(verbose_name=_('featured'))
    in_stock = models.BooleanField(verbose_name=_('in stock'), default=True)
    info = models.CharField(verbose_name=_('info'), blank=True, null=True, max_length=250)
    label = models.CharField(verbose_name=_('label'), blank=True, null=True, max_length=100)
    order_link = models.URLField()

    group = models.ForeignKey(ProductGroup)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Price(models.Model):
    """Price model."""
    PRICING_TYPE_CHOICES = (
        (conf.PricingType.HOURLY, _('Hourly')),
        (conf.PricingType.MONTHLY, _('Monthly')),
        (conf.PricingType.QUARTERLY, _('Quarterly')),
        (conf.PricingType.SEMI_ANNUALLY, _('Semi-Annually')),
        (conf.PricingType.ANNUALLY, _('Annually')),
        (conf.PricingType.BIENNIALLY, _('Biennially')),
        (conf.PricingType.TRIENNIALLY, _('Triennially')),
    )
    currencies = models.ManyToManyField(MoneyCurrency)
    pricing_type = models.IntegerField(
        verbose_name=_('pricing type'),
        choices=PRICING_TYPE_CHOICES,
    )
    product = models.ForeignKey(Product)
    price = models.DecimalField(
        verbose_name=_('price'),
        decimal_places=6,
        max_digits=10,
    )

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')
        ordering = ('pricing_type', )

    def __str__(self):
        return '{price} / {pricing_type}'.format(
            price=self.price, pricing_type=self.get_pricing_type_display()
        )

    @property
    def prices(self):
        prices = {}
        for currency in self.currencies.all():
            total_amount = currency.rate * self.price
            currency_parser = currency.get_currency_parser()

            prices[currency.currency] = {
                'total_amount': total_amount,
                'money_format': currency_parser.get_money_format(total_amount),
                'money_with_currency_format': currency_parser.get_money_with_currency_format(total_amount),
            }

        return prices


class Team(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(verbose_name=_('name'), max_length=100)
    bio = models.TextField(verbose_name=_('bio'))
    picture = FilerImageField(verbose_name=_('image'), blank=True, null=True)
    date_joined = models.DateField(verbose_name=_('date joined'))

    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')
        ordering = ('date_joined', )

    def __str__(self):
        return self.name


class Section(models.Model):
    """Section model."""
    name = models.CharField(
        verbose_name=_('name'),
        max_length=250,
        help_text=_('Internal user only.')
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=250,
        help_text=_(
            'Public title of the section, visitors will be able to see it.',
        )
    )
    sub_title = models.CharField(
        verbose_name=_('sub title'),
        max_length=250,
        blank=True,
        null=True,
    )
    description = HTMLField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )
    image = FilerImageField(
        related_name='images',
        verbose_name=_('image'),
        help_text=_('Can be used for background image or the whole section.'),
        blank=True,
        null=True
    )
    secondary_image = FilerImageField(
        related_name='secondary_images',
        verbose_name=_('secondary image'),
        blank=True,
        null=True,
    )
    css_classes = models.CharField(
        verbose_name=_('css classes'),
        max_length=25,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    def __str__(self) -> str:
        return self.name


class SectionItem(models.Model):
    """Section Item."""
    section = models.ForeignKey(Section, related_name='items')
    title = models.CharField(verbose_name=_('title'), max_length=250)
    description = HTMLField(
        verbose_name=_('description'),
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
    icon_color = ColorField(blank=True, null=True)
    image = FilerImageField(verbose_name=_('image'), blank=True, null=True)
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
    item_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Section Items')
        ordering = ('item_order',)

    def __str__(self) -> str:
        return f'{self.title} | {self.section}'

    @property
    def link(self) -> Union[str, None]:
        link = None

        if self.internal_link:
            link = self.internal_link.get_absolute_url()

        if self.external_link:
            link = self.external_link

        return link


# CMS Plugin Models
class ProductGroupPlugin(CMSPlugin):
    """Product Group Plugin Model."""
    product_group = models.ForeignKey(ProductGroup)

    def __str__(self):
        return self.product_group.name


class TeamPlugin(CMSPlugin):
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.team.name


class TeamMemberPlugin(CMSPlugin):
    team_member = models.ForeignKey(TeamMember)

    def __str__(self):
        return self.team_member.name


class SectionPlugin(CMSPlugin):
    """Section CMS Plugin model."""
    section = models.ForeignKey(Section)
    template = models.CharField(verbose_name=_('template'), max_length=100)

    def __str__(self) -> str:
        return self.section.name


class CoverPlugin(CMSPlugin):
    """Cover Model."""
    title = models.CharField(
        verbose_name=_('title'),
        max_length=250,
        blank=True,
        null=True,
    )
    sub_title = models.CharField(
        verbose_name=_('sub title'),
        max_length=500,
        blank=True,
        null=True,
    )
    image = FilerImageField(verbose_name=_('image'), blank=True, null=True, related_name='cover_image')
    inside_image = FilerImageField(verbose_name=_('inside image'), blank=True, null=True, related_name='inside_image')
    detail = HTMLField(verbose_name=_('detail'), blank=True, null=True)
    is_scroll = models.BooleanField(verbose_name=_('is scroll'), default=False)

    @property
    def has_content(self):
        if self.title or self.sub_title or self.inside_image:
            return True
        return False

    def __str__(self):
        return self.title or ''
