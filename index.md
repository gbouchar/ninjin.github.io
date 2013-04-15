---
layout:         index
title:          Welcome!
cmeta:          "Homepage of your run-of-the-mill Ph.D. student in
                Natural Language Processing (NLP), contains:
                my publication list, blog posts, reflections on life
                and your occasional rant."
---

My name is Pontus Stenetorp (well, technically my name is Pontus Lars Erik
Saito Stenetorp or 西東　ステネートルプ　ポントス　ラース　エリック if you
prefer, but buy me a drink some time and I will tell you all about how I ended
up with possible the longest name in Japan and what it does to your average
company customer database), I am a special project research associate at the
[National Institute of Informatics][nii] and a visiting researcher at the
[University of Tokyo][todai].
To the right is a not-so-pleasing picture of me and my beloved late dog (she
looked a lot better than me that day).

I was raised in [a land of snow and beautiful summers][sweden] in a [small
town that most people have never heard of][lindesberg] (and for good reasons),
attended [Kungliga Tekniska högskolan][kth] (Royal Institute of Technology) in
Stockholm and received the degree of Master in Science and Engineering in
Computer Science in 2010.
I then joined the [Tsujii Laboratory][tsujii] at the [University of
Tokyo][todai] and was a member until the official closing of the lab in 2011
and then spent the remainder of my Ph.D. until my graduation in the spring of
2013 as a member of the [Aizawa Laboratory][aizawa], also at the [University
of Tokyo][todai].

The topic of my research is almost solely [Natural Language Processing][nlp]
(NLP), which is the task of processing text from sources such as newspapers,
blogs, etc. using computers.
[Carl Sagan][sagan] once said that writing allows humans to transfer
knowledge between individuals across time and space, a feat which is truly
incredible.
We humans describe our experiences in words, a form computers still have
difficulties to grasp due to it's frequently ambiguous nature, I thus see my
line of research as an attempt to tap into this vast source of knowledge.

As with most researchers I have several topics of interests in my field such
as Information Extraction (IE), computational lexical semantics and
extrinsic/intrinsic evaluation of NLP systems.
I am also active in the sub-field of Biomedical Natural Language Processing
(BioNLP) which I find to be an interesting application of NLP techniques.
On the side I dabble in and read a wide array of topics such as evolutionary
linguistics, computer security.
If you share any of my interests you may want to have a glance at my hopefully
growing [list of publications][publications].

During what spare time I have left after, I enjoy tinkering with computers, producing
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
[nii]:          http://www.nii.ac.jp/en/
[nlp]:          https://en.wikipedia.org/wiki/Natural_language_processing
[publications]: /publications.html
[sagan]:        https://en.wikipedia.org/wiki/Carl_Sagan
[sweden]:       http://en.wikipedia.org/wiki/Sweden
[todai]:        http://www.u-tokyo.ac.jp/index_e.html
[tsujii]:       http://www.nactem.ac.uk/tsujii/
