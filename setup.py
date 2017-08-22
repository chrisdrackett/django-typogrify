# -*- coding: utf-8 -*-
from setuptools import setup

VERSION = '1.3.3'

setup(
    name='django-typogrify',
    version=VERSION,
    description='Make type not look like crap (for django apps)',
    author='Chris Drackett',
    author_email='chris@tiltshiftstudio.com',
    url='http://github.com/chrisdrackett/django-typogrify',
    packages=[
        "typogrify",
        "typogrify.templatetags",
    ],
    install_requires=[
        'smartypants>=1.8.3', 'num2words'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        # 'Intended Audience :: Designers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
        'Topic :: Text Processing'
    ],
)
