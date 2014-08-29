#!/usr/bin/env python3
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

'''
Convert BibTeX-files to Jekyll posts for my personal homepage.

Author:     Pontus Stenetorp    <pontus stenetorp se>
Version:    2014-01-18
'''

from argparse import ArgumentParser
from argparse import FileType
from datetime import date
from datetime import datetime
from os.path import join as path_join
from sys import stderr
from sys import stdin
from sys import stdout

from pybtex.database.input.bibtex import Parser as BibTeXParser

### Constants
SELECTED = set((
    'stenetorp2013transition',
    'stenetorp2012brat',
    ))
# Not even nearly exhaustive, a hack.
TEX_UNESCAPES = (
        # Note: Font support is terrible for these two.
        ("\\'{c}", 'c', ),
        ('\\u{g}', 'g', ),

        ("\\'{e}", 'e', ),
        ('\\"{u}', 'ü', ),
        ('\\textsc{', '', ),
        ('{', '', ),
        ('}', '', ),
        )
###

def _argparser():
    argparser = ArgumentParser()

    argparser.add_argument('posts_dir', help='directory for generated posts')
    argparser.add_argument('bibs', type=FileType('r'), nargs='+',
            help='BibTeX-files to convert')

    argparser.add_argument('-i', '--input', type=FileType('r'),
            default=stdin, help='input source (default: stdin)')
    argparser.add_argument('-o', '--output', type=FileType('w'),
            default=stdout, help='output target (default: stdout)')

    return argparser

def _tex_unescape(s):
    for _from, to in TEX_UNESCAPES:
        s = s.replace(_from, to)
    return s

def _authors(s):
    for author in s.split(' and '):
        last, first = author.split(', ')
        yield '{} {}'.format(first, last)

def main(args):
    argp = _argparser().parse_args(args[1:])

    for bib in argp.bibs:
        soup = BibTeXParser().parse_stream(bib)

        if len(soup.entries) < 1:
            print('WARNING: "{}" contains no entries, skipping.'.format(
                bib.name), file=stderr)
            continue

        entries = soup.entries
        for entry in entries:
            # Note: This library is really object oriented from hell.
            fields = entries[entry].fields

            year = datetime.strptime(fields['year'], '%Y').year
            month = datetime.strptime(fields['month'], '%B').month
            day = datetime.strptime(fields['day'], '%d').day
            presented = date(year=year, month=month, day=day)

            post_fname = '{}-{}.md'.format(
                    presented.strftime('%Y-%m-%d'), entry)

            out = [
                    '---',
                    '# Note: Generated file, do not edit directly.',
                    'type: publication',
                    'bib: {}'.format(repr('/' + bib.name)),
                    'title: {}'.format(repr(_tex_unescape(fields['title']))),
                    'authors: [{}]'.format(
                        ','.join(repr(a) for a in _authors(
                            _tex_unescape(fields['author'])))),
                    ]

            try:
                out.append('venue_type: {}'.format(
                        repr(fields['venue_type'].lower())))
            except KeyError:
                out.append('venue_type: international')

            try:
                out.append('venue: {}'.format(
                    repr(_tex_unescape(fields['booktitle']))))
            except KeyError:
                pass

            try:
                out.append('location: {}'.format(
                    repr(_tex_unescape(fields['address']))))
            except KeyError:
                pass

            try:
                out.append('school: {}'.format(repr(fields['school'])))
            except KeyError:
                pass

            try:
                out.append('pdf: {}'.format(repr(fields['pdf_url'])).replace(
                    # Make the URL reference local.
                    'http://pontus.stenetorp.se', ''))
            except KeyError:
                pass

            try:
                out.append('slides: "{}"'.format(fields['slides_url']).replace(
                    # Make the URL reference local.
                    'http://pontus.stenetorp.se', ''))
            except KeyError:
                pass

            try:
                out.append('poster: "{}"'.format(fields['poster_url']
                    # Make the URL reference local.
                    ).replace('http://pontus.stenetorp.se', ''))
            except KeyError:
                pass

            try:
                out.append('pages: "{}"'.format(
                    fields['pages'].replace('--', '-')))
            except KeyError:
                pass

            try:
                out.append('publisher: "{}"'.format(fields['publisher']))
            except KeyError:
                pass

            if entry in SELECTED:
                out.append('selected: true')

            try:
                if fields['note'].lower() == 'to appear':
                    out.append('to_appear: true')
            except KeyError:
                pass

            out.append('---\n')

            with open(path_join(argp.posts_dir, post_fname), 'w') as post:
                post.write('\n'.join(out))

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
