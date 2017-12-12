from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cmsplugin_pure_text.models import PureText


@plugin_pool.register_plugin
class PureTextPluginPublisher(CMSPluginBase):
    model = PureText
    name = _('Pure Text Plugin')
    render_template = 'cmsplugin_pure_text/pure_text.txt'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
