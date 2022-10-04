from django import template

register = template.Library()


@register.filter("hideemail")
def hideemail(obj):
    return obj.replace(obj[3:10], "****")

@register.filter("hidephone")
def hidephone(obj):
    return obj.replace(obj[:-4], "******")
