typogrify: Django template filters to make web typography easier
================================================================

This application provides a set of custom filters for the Django
template system which automatically apply various transformations to
plain text in order to yield typographically-improved HTML.

Requirements
============

typogrify is designed to work with Django, and so requires a
functioning installation of Django 0.96 or later.

* **Django**: http://www.djangoproject.com/
* **Textile**: http://github.com/chrisdrackett/python-textile

Installation
============

1. checkout the project into a folder called `typogrify` on your python path:

    git clone git@github.com:chrisdrackett/django-typogrify.git typogrify

2. Add 'typogrify' to your INSTALLED_APPS setting.


Included filters
================

amp
---

Wraps ampersands in HTML with <span class="amp"> so they can be
styled with CSS. Ampersands are also normalized to &amp;. Requires
ampersands to have whitespace or an &nbsp; on both sides. Will not
change any ampersand which has already been wrapped in this fashion.

caps
----

Wraps multiple capital letters in <span class="caps"> so they can
be styled with CSS.

initial_quotes
--------------

Wraps initial quotes in <span class="dquo"> for double quotes or
<span class="quo"> for single quotes. Works inside these block
elements:

* h1, h2, h3, h4, h5, h6
* p
* li
* dt
* dd

Also accounts for potential opening inline elements: a, em,
strong, span, b, i.

smartypants
-----------

* Straight quotes ( " and ' ) into “curly” quote HTML entities (&lsquo; | &rsquo; | &ldquo; | &rdquo;)
* Backticks-style quotes (``like this'') into “curly” quote HTML entities (&lsquo; | &rsquo; | &ldquo; | &rdquo;)
* Dashes (“--” and “---”) into n-dash and m-dash entities (&ndash; | &mdash;)
* Three consecutive dots (“...”) into an ellipsis entity (&hellip;)

widont
------

Based on Shaun Inman's PHP utility of the same name, replaces the
space between the last two words in a string with &nbsp; to avoid
a final line of text with only one word.

Works inside these block elements:

* h1, h2, h3, h4, h5, h6
* p
* li
* dt
* dd

Also accounts for potential closing inline elements: a, em,
strong, span, b, i.

titlecase
---------

http://daringfireball.net/2008/05/title_case

number_suffix
-------------

wraps number suffix's in <span class="ord"></span> so they can be styled.

fuzzydate
---------
(uses code from http://djangosnippets.org/snippets/1347/)

Returns the date in a more human readable format:

* Today
* Yesterday
* 4 days ago
* 3 weeks ago
* in 3 years
* etc.

typogrify
---------

Applies all of the following filters, in order:

* force_unicode (from django.utils.encoding)
* amp
* widont
* smartypants
* caps
* initial_quotes
