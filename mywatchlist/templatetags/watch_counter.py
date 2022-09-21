from django import template

register = template.Library()

@register.filter
def count_watched(film):
    return sum([x.watched for x in film])

@register.filter
def count_all_divided_by_two(film):
    return ((sum([x.watched for x in film]) + sum([not x.watched for x in film]))/2)