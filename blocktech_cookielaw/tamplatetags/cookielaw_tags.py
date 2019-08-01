from django import template
from classytags.helpers import InclusionTag
from django.template.loader import render_to_string

register = template.Library()


class CookielawBanner(InclusionTag):
    template = "blocktech_cookielaw/banner.html"

    def render_tag(self, context, **kwargs):
        template_filename = self.get_template(context, **kwargs)

        return render_to_string(template_filename, data, context.request)


register.tag(CookielawBanner)
