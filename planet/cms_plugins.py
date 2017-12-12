from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from planet.forms import SectionPluginPublisherForm
from planet.models import (
    ProductGroupPlugin,
    TeamPlugin,
    TeamMemberPlugin,
    SectionPlugin,
    CoverPlugin,
)


@plugin_pool.register_plugin
class ProductGroupPluginPublisher(CMSPluginBase):
    model = ProductGroupPlugin
    name = _('Product Group')
    render_template = 'planet/cms/product_group.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class TeamPluginPublisher(CMSPluginBase):
    model = TeamPlugin
    name = _('Team')
    render_template = 'planet/cms/team.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class TeamMemberPluginPublisher(CMSPluginBase):
    model = TeamMemberPlugin
    name = _('Team Member')
    render_template = 'planet/cms/team_member.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class SectionPluginPublisher(CMSPluginBase):
    model = SectionPlugin
    form = SectionPluginPublisherForm
    name = _('Section')
    render_template = 'planet/cms/sections/feature_icon.html'

    def render(self, context, instance: SectionPlugin, placeholder):
        self.render_template = instance.template
        context.update({'instance': instance})

        return context


@plugin_pool.register_plugin
class CoverPluginPublisher(CMSPluginBase):
    model = CoverPlugin
    name = _('Cover Plugin')
    render_template = 'planet/cms/cover.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
