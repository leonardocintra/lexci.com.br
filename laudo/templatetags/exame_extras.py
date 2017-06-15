from django import template

register = template.Library()

@register.filter
def replace_nome_exame(string_nome):
    return string_nome.replace(" ", "_").lower()