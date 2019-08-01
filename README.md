# django-bt-cookielaw


```.python
INSTALLED_APPS = [
    ...
    "blocktech_cookielaw",
    ...
]

```


## in django template
```.html
{% load cookielaw_tags %}


{% cookie_law_banner %}

```