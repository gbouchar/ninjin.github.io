---
layout:         index
title:          Welcome!
cmeta:          "Homepage of your run-of-the-mill Ph.D. student in
                Natural Language Processing (NLP), contains:
                my publication list, blog posts, reflections on life
                and your occasional rant."
---

My name is Pontus Stenetorp, I am a second year Ph.D. student at the [Aizawa
Laboratory][aizawa] at [The University of Tokyo][todai] in Tokyo, Japan. To
the right is a not-so-pleasing picture of me and my dog (she looks better than
me on this occasion).

My research interests is primarily in the domain of Biomedical Natural
Language Processing (BioNLP), but I also have a great deal of interest in
evolutionary linguistics, in particular in relation to changes in vocabulary.
If you are interested you can have a glance at my hopefully growing [list of
publications][publications].

I was raised in [a land of snow and beautiful summers][sweden] in a [small
town that most people have never heard of][lindesberg] (and for good reasons),
attended [Kungliga Tekniska högskolan][kth] (The Royal Institute of
Technology) in Stockholm and received the degree of Master in Science and
Engineering in Computer Science.

During what spare time I have left, I enjoy tinkering with computers, producing
code for fun, [hacking on an operating system][freebsd], biking, traveling and
photography. My [Erdős number][erdos] is 5 (Me -> J. J. Li -> T. Kowalski ->
P. Jipsen -> Z. Tuza -> P. Erdős).

## Recent News ##

{% for post in site.posts %}
    {% if post.categories contains 'news' %}

### {{ post.date | | date:'%Y-%m-%d' }}: {{ post.title }}  ###

{{ post.content }}

    {% endif %}
{% endfor %}

[aizawa]:       http://www-al.nii.ac.jp/en/index.html
[erdos]:        http://en.wikipedia.org/wiki/Erd%C5%91s_number
[freebsd]:      http://www.freebsd.org/
[kth]:          http://www.kth.se/?l=en_UK
[lindesberg]:   http://en.wikipedia.org/wiki/Lindesberg
[publications]: /publications.html
[sweden]:       http://en.wikipedia.org/wiki/Sweden
[todai]:        http://www.u-tokyo.ac.jp/index_e.html
