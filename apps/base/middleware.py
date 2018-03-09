#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
@version: v1.0
@author: cm
@time: 09/03/2018 1:46 PM
"""

from django.http import Http404
from .models import Tenant


def remove_www(hostname):
    """
    Removes www. from the beginning of the address. Only for
    routing purposes. www.test.com/login/ and test.com/login/ should
    find the same tenant.
    """
    if hostname.startswith("www."):
        return hostname[4:]

    return hostname


class BaseTenantMiddleware(object):
    TENANT_NOT_FOUND_EXCEPTION = Http404

    def get_tenant(self, model, hostname, request):
        raise NotImplementedError

    def hostname_from_request(self, request):
        """ Extracts hostname from request. Used for custom requests filtering.
            By default removes the request's port and common prefixes.
        """
        return remove_www(request.get_host().split(':')[0]).lower()

    def process_request(self, request):
        hostname = self.hostname_from_request(request)

        try:
            tenant = self.get_tenant(Tenant, hostname, request)
            assert isinstance(tenant, Tenant)
        except Tenant.DoesNotExist:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                'No tenant for {!r}'.format(request.get_host()))
        except AssertionError:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                'Invalid tenant {!r}'.format(request.tenant))

        request.tenant = tenant

        # Do we have a public-specific urlconf?
        if hasattr(settings, 'PUBLIC_SCHEMA_URLCONF') and request.tenant.schema_name == get_public_schema_name():
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF
