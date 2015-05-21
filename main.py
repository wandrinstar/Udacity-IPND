#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
import cgi
from google.appengine.ext import ndb
from html_generator import get_stage_html
from notes import all_stages

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
jinja_env.globals['get_stage_html'] = get_stage_html

class Comment(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    stage = ndb.IntegerProperty(indexed=True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        template = jinja_env.get_template(template)
        return template.render(params)

    def render_page(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def show_page(self, template, stage_notes=None, stage_num=None, path='/'):
        cursor = Comment.query(Comment.stage==stage_num).order(-Comment.date)
        user_comments = cursor.fetch()

        if stage_num is not None:
            previous_path = path[0:-1] + str(stage_num-1)
            next_path = path[0:-1] + str(stage_num+1)
            if stage_num < 1:
                previous_path = None
            if stage_num > len(all_stages)-2:
                next_path = None
        else:
            next_path = None
            previous_path = None

        self.render_page(template, stage_notes=stage_notes, user_comments=user_comments,  previous_path=previous_path, next_path=next_path)

    def post_comment(self, template, stage_num=None, path='/'):
        content = cgi.escape(self.request.get('comment'), quote=True)
        self.comment = Comment(content=content, stage=stage_num)
        if content:
            self.comment.put()
        path += '#comments'
        self.redirect(path)

class Home(Handler):
    def get(self):
        self.show_page('home.html')

    def post(self):
        self.post_comment('home.html')

class Stage(Handler):

    def get(self):
        path = self.request.path
        stage_num = int(path[-1])
        self.show_page('stage.html', all_stages[stage_num], stage_num, path)

    def post(self):
        path = self.request.path
        stage_num = int(path[-1])
        self.post_comment('stage.html', stage_num, path)

app = webapp2.WSGIApplication([('/', Home),
                               ('/home', Home),
                               ('/stage0', Stage),
                               ('/stage1', Stage),
                                ('/stage2', Stage),
                                ('/stage3', Stage),
                                ('/stage4', Stage)
                               ], debug=True)


