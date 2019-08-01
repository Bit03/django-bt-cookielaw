import os
from itertools import chain
from glob import glob

from setuptools import setup, find_packages

import blocktech_cookielaw

package_data_globs = (
    'blocktech_cookielaw/templates/cookielaw/*.html',
    'blocktech_cookielaw/static/cookielaw/*/*',
)

package_data = []
for f in chain(*map(glob, package_data_globs)):
    package_data.append(f.split('/', 1)[1])

setup(
    author='jiaxin',
    author_email='edison7500@gmail.com',
    name='django-bt-cookielaw',
    version=blocktech_cookielaw.__version__,
    description='Helps your Django project comply with EU cookie law regulations',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/edison7500/django-bt-cookielaw',
    license='GUN License',
    platforms=['OS Independent'],
    install_requires=[
        'Django>=1.11',
        'django-classy-tags>=0.3.0',
    ],
    packages=find_packages(),
    package_data={'blocktech_cookielaw': package_data},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
