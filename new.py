#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2014 Mitchell Barry
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = "Mitchell Barry"
__email__ = "mitch.barry@gmail.com"

import os
import sys
import time
import datetime

"""
Python script to add new content to Pelican site with proper metadata
for Markdown style content
"""

content_dir = 'content'
default_category = 'misc'
about_author = 'Software Developer, Person'


class ContentBuilder:
    filename = ''
    title = ''
    slug = ''
    category = ''
    tags = []
    summary = ''
    author_summary = ''

    def __init__(self, **kwargs):
        self.filename = self.get_text_input(
            prompt='FileName: ',
            suggestion=None)
        self.title = self.get_text_input(
            prompt='Title: ',
            suggestion=None)
        self.slug = self.get_text_input(
            prompt='Slug: ',
            suggestion=self.format_slug(self.title))
        self.category = self.get_text_input(
            prompt='Category: ',
            suggestion=default_category)
        self.get_tags()
        self.summary = self.get_text_input(
            prompt='Summary: ',
            suggestion=None)
        self.author_summary = self.get_text_input(
            prompt='About Author: ',
            suggestion=about_author)

        if self.confirm():
            self.create_file()
        else:
            print 'Exiting...\n'

    def confirm(self):
        print 'About to write new file: \n'
        print 'FileName: %s' % self.filename
        print 'Title: %s' % self.title
        print 'Slug: %s' % self.slug
        print 'Category: %s' % self.category
        print 'Tags: %s' % str(self.tags)
        print 'Summary: %s' % self.summary
        print 'About_Author: %s' % self.author_summary
        return raw_input('Is the above information correct? [y/N] ').upper() == 'Y'

    def create_file(self):
        filepath = '{0}/{1}/{2}.md'.format(
            content_dir,
            self.category,
            self.filename)
        now = datetime.datetime.now()
        print 'Creating file... {0}'.format(filepath)

        directory = '{0}/{1}'.format(content_dir, self.category)
        if not os.path.exists(directory):
            print 'creating new category...'
            os.makedirs(directory)
        f = open(filepath, 'w')
        f.write('Title: %s\n' % self.title)
        f.write('Date: %s\n' % now.strftime('%Y-%m-%d %H:%M'))
        f.write('Modified: %s\n' % now.strftime('%Y-%m-%d %H:%M'))
        f.write('Tags: %s\n' % ','.join(self.tags))
        f.write('Slug: %s\n' % self.slug)
        f.write('Summary: %s\n' % self.summary)
        f.write('About_author: %s\n' %s self.author_summary)
        f.write('\n')
        f.close()
        print 'File created!'


    def format_slug(self, title):
        return title.replace(' ', '-').lower()

    def get_text_input(self, prompt, suggestion=None):
        if suggestion:
            prompt = '{0} [{1}] '.format(prompt, suggestion)
        user_input = raw_input(prompt)
        if not user_input:
            user_input = suggestion
        return user_input

    def get_tags(self):
        i = 0
        tag = ''
        while tag != '' or i == 0:
            i += 1
            if tag:
                self.tags.append(tag)
            tag = raw_input('Tags [blank to stop]: ')


if __name__ == '__main__':
    builder = ContentBuilder()

#Title: Test Welcome
#Date: 2014-08-08 10:53
#Modified: 2014-08-08 10:53
#Tags: blog
#Slug: welcome
#Summary: The new home for me on the Internet
