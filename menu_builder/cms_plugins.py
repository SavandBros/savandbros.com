from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from menu_builder.models import MenuPlugin


@plugin_pool.register_plugin
class MenuPluginPublisher(CMSPluginBase):
    model = MenuPlugin
    name = _('Menu')
    render_template = 'menu_builder/menu.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
