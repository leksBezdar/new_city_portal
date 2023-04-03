from django import template
from api.models import *
register = template.Library()


@register.inclusion_tag('api/menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    }


@register.inclusion_tag('api/post.html', takes_context=True)
def show_post(context):
    post_items = Post.objects.latest('time_update')
    return {
        "post_items": post_items,
    }
