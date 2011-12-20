---
layout: base
title: News
---

# {{ page.title }} #

This page covers news regarding the site and me in general that won't qualify
for a blog post of any kind.

{% for post in site.posts %}
    {% if post.categories contains 'news' %}

## {{ post.date | | date:'%Y-%m-%d' }}: {{ post.title }}  ##

{{ post.content }}

    {% endif %}
{% endfor %}
