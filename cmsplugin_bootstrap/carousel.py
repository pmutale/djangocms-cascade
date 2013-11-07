# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cmsplugin_bootstrap.change_form_widgets import ExtraStylesWidget, MultipleRadioButtonsWidget
from cmsplugin_bootstrap.plugin_base import BootstrapPluginBase, CSS_MARGIN_STYLES


class CarouselPlugin(BootstrapPluginBase):
    name = _("Carousel")
    render_template = "cms/plugins/bootstrap/carousel.html"
    child_classes = ['SlidePlugin']
    css_class_choices = (('slide', 'slide'),)
    extra_styles_widget = ExtraStylesWidget(CSS_MARGIN_STYLES + ['width', 'height'])
    options_widget = ExtraStylesWidget(['interval', 'slide-to'])

plugin_pool.register_plugin(CarouselPlugin)


class SlidePlugin(BootstrapPluginBase):
    name = _("Slide")
    parent_classes = ['CarouselPlugin']
    child_classes = ['TextPlugin', 'FilerImagePlugin']
    css_class_choices = (('item', 'item'),)

plugin_pool.register_plugin(SlidePlugin)