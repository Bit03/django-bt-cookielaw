import os

from setuptools import setup, find_packages

import blocktech_cookielaw

setup(
    author='jiaxin',
    author_email='edison7500@gmail.com',
    name='django-bt-cookielaw',
    version='.'.join(str(v) for v in blocktech_cookielaw.VERSION),
    description='Helps your Django project comply with EU cookie law regulations',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/edison7500/django-bt-cookielaw',
    license='GUN License',
    platforms=['OS Independent'],
    # classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.11',
        'django-classy-tags>=0.3.0',
    ],
    packages=find_packages(),
    # package_data={'cookielaw': package_data},
    include_package_data=False,
    zip_safe=False,
    # test_suite='tests',
)