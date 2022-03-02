from django.utils.translation import ugettext_lazy as _

from .production import *


CONVERT_UTC_TO_TIME_ZONE = True

COURSE_MODE_DEFAULTS = {
    'bulk_sku': None,
    'currency': 'vnd',
    'description': None,
    'expiration_datetime': None,
    'min_price': 0,
    'name': _('Audit'),
    'sku': None,
    'slug': 'audit',
    'suggested_prices': '',
}
