# Makefile for Jekyll interactions that I just can't be bothered to remember.
#
# Author:	Pontus Stenetorp	<pontus stenetorp se>
# Version:	2014-01-08

### From: https://help.github.com/articles/using-jekyll-with-pages
.PHONY: serve
serve:
	bundle exec jekyll serve --watch

.PHONY: install
install:
	sudo gem install bundler
	bundle install

.PHONY: update
update:
	bundle update
