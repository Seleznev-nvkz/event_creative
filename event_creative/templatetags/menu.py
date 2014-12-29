from django.core.urlresolvers import resolve, Resolver404
from django import template

register = template.Library()


@register.simple_tag
def active_url(request, urls):
    try:
        view = resolve(request.path).url_name
        if view in urls:
            return "current_page_item"
        else:
            return ""
    except Resolver404:
        return ""