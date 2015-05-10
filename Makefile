# Makefile for Jekyll interactions that I just can't be bothered to remember.
#
# Author:	Pontus Stenetorp	<pontus stenetorp se>
# Version:	2014-01-08

# From: https://help.github.com/articles/using-jekyll-with-pages
.PHONY: serve
serve:
	bundle exec jekyll serve --watch

.PHONY: imgopt
imgopt:
	find img -name '*.jpg' | xargs -r jpegoptim
	find img -name '*.png' | xargs -r optipng

.PHONY:	bibposts
bibposts:
	./bib2post.py _posts/ res/bib/*.bib.txt

# Necessary tools to build the homepage.
.PHONY: deps
deps:
	sudo apt-get install jpegoptim libz-dev optipng ruby ruby-dev python3 \
		python3-pip
	sudo pip3 install pybtex
	sudo gem install bundler
	bundle install

.PHONY: update
update:
	bundle update
