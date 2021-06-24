from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    return float(value) * arg


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='placeholder')
def addplaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})


@register.filter(name='times')
def times(number):
    nm = int(number)
    return range(nm)


@register.filter(name='addplaceholder')
def html_placeholder(field, args=None):
    if args is None:
        return field
    field.field.widget.attrs.update({"placeholder": args})
    return field
