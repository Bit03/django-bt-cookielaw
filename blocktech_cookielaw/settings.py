from django.conf import settings

_default_js = ('blocktech_cookielaw/js/cookielaw.js',)

BLOCKTECH_COOKIELAW_JS = getattr(settings, 'BLOCKTECH_COOKIELAW_JS', _default_js)
BLOCKTECH_COOKIELAW_CSS = getattr(settings, 'BLOCKTECH_COOKIELAW_CSS', {})
