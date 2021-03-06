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

makefile = """PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=__SSH_HOST__
SSH_PORT=__SSH_PORT__
SSH_USER=__SSH_USER__
SSH_TARGET_DIR=__SSH_TARGET_DIR__

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
\tPELICANOPTS += -D
endif

help:
\t@echo 'Makefile for a pelican Web site                                        '
\t@echo '                                                                       '
\t@echo 'Usage:                                                                 '
\t@echo '   make html                        (re)generate the web site          '
\t@echo '   make clean                       remove the generated files         '
\t@echo '   make regenerate                  regenerate files upon modification '
\t@echo '   make publish                     generate using production settings '
\t@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
\t@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
\t@echo '   make stopserver                  stop local server                  '
\t@echo '   make ssh_upload                  upload the web site via SSH        '
\t@echo '   make rsync_upload                upload the web site via rsync+ssh  '
\t@echo '   make dropbox_upload              upload the web site via Dropbox    '
\t@echo '   make ftp_upload                  upload the web site via FTP        '
\t@echo '   make s3_upload                   upload the web site via S3         '
\t@echo '   make cf_upload                   upload the web site via Cloud Files'
\t@echo '   make github                      upload the web site via gh-pages   '
\t@echo '                                                                       '
\t@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
\t@echo '                                                                       '

html:
\t$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
\t[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
\t$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
\tcd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
\tcd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
\t$(BASEDIR)/develop_server.sh restart $(PORT)
else
\t$(BASEDIR)/develop_server.sh restart
endif

stopserver:
\tkill -9 `cat pelican.pid`
\tkill -9 `cat srv.pid`
\t@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
\t$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
\tscp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
\trsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
\tcp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
\tlftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
\ts3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type

cf_upload: publish
\tcd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
\tghp-import -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
\tgit push origin $(GITHUB_PAGES_BRANCH)

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
"""

class MakefileBuilder:
    host = ''
    port = ''
    user = ''
    directory = ''

    def __init__(self):
        self.host = self.get_text_input(
            prompt='Host: ',
            suggestion=None)
        self.port = self.get_text_input(
            prompt='Port: ',
            suggestion='22')
        self.user = self.get_text_input(
            prompt='User: ',
            suggestion=None)
        self.directory = self.get_text_input(
            prompt='Directory: ',
            suggestion='/var/www')

        if self.confirm():
            self.create_file()
        else:
            print 'Exiting...\n'

    def get_text_input(self, prompt, suggestion=None):
        if suggestion:
            prompt = '{0} [{1}] '.format(prompt, suggestion)
        user_input = raw_input(prompt)
        if not user_input:
            user_input = suggestion
        return user_input

    def confirm(self):
        print 'About to write Makefile: \n'
        print 'SSH Host: %s' % self.host
        print 'SSH Port: %s' % self.port
        print 'SSH User: %s' % self.user
        print 'SSH Dir: %s' % self.directory
        return raw_input('Is the above information correct? [y/N] ').upper() == 'Y'

    def create_file(self):
        global makefile
        filepath = 'Makefile'
        print 'Creating file... {0}'.format(filepath)

        makefile = makefile.replace('__SSH_HOST__', self.host)
        makefile = makefile.replace('__SSH_PORT__', self.port)
        makefile = makefile.replace('__SSH_USER__', self.user)
        makefile = makefile.replace('__SSH_TARGET_DIR__', self.directory)

        f = open(filepath, 'w')
        f.write('%s\n' % makefile)
        f.close()
        print 'File created!'

if __name__ == '__main__':
    builder = MakefileBuilder()
