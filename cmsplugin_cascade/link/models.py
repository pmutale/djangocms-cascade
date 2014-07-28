# -*- coding: utf-8 -*-
from django.db.models import get_model
from django.core.exceptions import ObjectDoesNotExist
from cmsplugin_cascade.models import CascadeElement


class LinkElement(CascadeElement):
    """
    A model class to adding an internal or external Link plus a glossary.
    """
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.name

    @property
    def link(self):
        link = self.glossary.get('link', {})
        if 'model' in link:
            Model = get_model(*link['model'].split('.'))
            try:
                obj = Model.objects.get(pk=link['pk'])
                return obj.get_absolute_url()
            except ObjectDoesNotExist:
                pass
        if link.get('type') == 'exturl':
            return link['url']
        if link.get('type') == 'email':
            return 'mailto:{email}'.format(**link)
        return '#'

    @property
    def name(self):
        return self.glossary.get('link_content', '')
