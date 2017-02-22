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
import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t= jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    submitted_dt = db.DateTimeProperty(auto_now_add = True)
    modified_dt = db.DateTimeProperty(auto_now = True)


class Permalink(Handler):
    def get(self, id):
        s= ""
        post = Post.get_by_id(int(id))
        s = s + post.title + "<br>" + "<hr>"

        s = s + post.content + "<br>" + "<br><br>"

        header = "<h2>Mang's Blog</h2>"
        form = ("<form method ='post' action='/'>" + s + id + "</form>")
        self.response.write(header + form)

class NewPosts(webapp2.RequestHandler):
    def render_newpost(self, title="", content="", error= ""):
        t = jinja_env.get_template("newpost.html")
        response = t.render(title=title, content=content, error=error)
        self.response.out.write(response)
        #self.render("newpost.html",title=title,content=content,error= error)

    def get(self):
        self.render_newpost()

    def post(self):
        title = self.request.get("title")
        content = self.request.get("content")

        if title and content:
            p = Post(title = title, content = content)
            p.put()
            #self.redirect('/blog/id=%s' % str(p.key().id()))
            id = p.key().id()
            self.redirect('/blog/%s' % id)
        else:
            error = "We need both title and content!"
            self.redirect("newpost.html",title=title,content=content,error= error)

            #self.render(title, content, error)

class MainblogHandler(Handler):
    def render_mainblog(self, title ="", content ="", error = ""):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY submitted_dt DESC Limit 5")
        s = ""
        for i in posts:
            s = s + i.title + "<div align='right'>" + str(i.submitted_dt) + "</div>"
            s = s + "<hr>"
            s = s + i.content + "<br>"

        self.render("mainblog.html",posts = posts)
        #self.response.write("Thanks")
        header = "<h2>Mang's Blog</h2>"
        form = ("<form method ='post' action='/'>" + s + "</form>")
        self.response.write(header + form)

    def get(self):
        self.render_mainblog()

app = webapp2.WSGIApplication(
[('/blog/newpost', NewPosts),
 ('/blog/', MainblogHandler),
 webapp2.Route('/blog/<id:\d+>', Permalink)
], debug=True)
