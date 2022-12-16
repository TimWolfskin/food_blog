from django import template
from contact.models import Social, About



register = template.Library()



@register.simple_tag()
def get_social_links():
    """displaying social links"""
    return Social.objects.all()



@register.simple_tag()
def get_about():
    """displaying about"""
    return About.objects.last()



