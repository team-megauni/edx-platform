from django.utils.translation import ugettext_lazy as _

from .production import *


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

CONVERT_UTC_TO_TIME_ZONE = ENV_TOKENS.get('CONVERT_UTC_TO_TIME_ZONE', True)

FRESHCHAT_TOKEN = ENV_TOKENS.get('FRESHCHAT_TOKEN', '')
FRESHCHAT_HOST = ENV_TOKENS.get('FRESHCHAT_HOST', '')
