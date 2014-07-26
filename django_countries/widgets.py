from django.conf import settings
from django.forms import widgets
from django.utils.safestring import mark_safe

COUNTRY_CHANGE_HANDLER = """
this.nextSibling.src = this.nextSibling.src.replace(/[a-z_]*\.gif/, (this.value.toLowerCase() || '__') + '.gif');
"""

FLAG_IMAGE = """<img style="margin: 6px 4px; position: absolute;" src="%sflags/%s.gif" id="%s-flag">"""


class CountrySelectWidget(widgets.Select):
    def render(self, name, value, attrs=None):
        attrs = attrs or {}
        attrs['onchange'] = COUNTRY_CHANGE_HANDLER
        data = super(CountrySelectWidget, self).render(name, value, attrs)
        data += mark_safe(FLAG_IMAGE % (
            settings.STATIC_URL,
            unicode(value).lower() or '__',
            attrs['id']
        ))
        return data
