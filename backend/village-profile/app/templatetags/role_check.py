from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='is_super_admin')
def is_super_admin(user):
    return user.groups.filter(name='superadmin')


@register.filter(name='is_admin')
def is_admin(user):
    if user.groups.filter(name='superadmin'):
        return user.groups.filter(name='superadmin')
    if user.groups.filter(name='admin'):
        return user.groups.filter(name='admin')


@register.filter(name='is_staff')
def is_staff(user):
    return user.groups.filter(name='staff')


@register.filter(name='my_group')
def my_group(user):
    if user.groups.filter(name='admin'):
        return 'Admin'
    if user.groups.filter(name='staff'):
        return 'Staff'
    return ''
