---
layout: human
title:  Feelings of an Almost Human Nature
cmeta:  "A blog about technology and life, musings of a curious character."
---

# {{ page.title }} #

Ramblings, musing and general non-sense regarding life, technology and
whatever may flow through my mind at this very moment. Rather than going
straight to */dev/null* I will try to pipe some output here. Expect chaos,
hope for order.

{% for post in site.posts %}
    {% if post.categories contains 'human' %}

## [{{ post.date | | date:'%Y-%m-%d' }}: {{ post.title }}]({{ post.url }})  ##

{{ post.content }}

    {% endif %}
{% endfor %}
