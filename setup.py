from setuptools import setup, find_packages
 
setup(
    name='django-typogrify',
    version='1.2',
    description='Make type not look like crap (for django apps)',
    author='Chris Drackett',
    author_email='chris@shelfworthy.com',
    url='http://github.com/chrisdrackett/django-typogrify',
    packages = [
        "typogrify",
        "typogrify.templatetags",
    ],
    install_requires = [
        'textile',
        'smartypants>=1.6'
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