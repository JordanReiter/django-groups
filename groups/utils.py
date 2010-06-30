from django.core.urlresolvers import reverse as django_reverse

def reverse(viewname, bridge=None, group=None, args=None, kwargs=None):
    if bridge and group:
        return bridge.reverse(viewname, group, kwargs=kwargs)
    else:
        return django_reverse(viewname, kwargs=kwargs)