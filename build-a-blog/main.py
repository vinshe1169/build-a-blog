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

    def render(self):
        self._render_text = self.content.replace('\n','<br>')
        return render_str("post.html",p = self)


class MainblogHandler(Handler):
    def get(self):
        self.render_mainblog()

    def render_mainblog(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY submitted_dt DESC Limit 5")
        self.render("mainblog.html",posts = posts)

class NewPostHandler(Handler):
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
            self.redirect('/blog/%s' % p.key().id())
        else:
            error = "We need both title and content!"
            self.render("newpost.html", title = title, content=content, error= error)
            #return render_newpost("newpost.html", title=title,content=content,error= error)
            

class PostPageHandler(Handler):
    def get(self,id):
        post = Post.get_by_id(int(id))
        self.render("permalink.html",post = post)

app = webapp2.WSGIApplication(
[('/blog', MainblogHandler),
('/blog/newpost', NewPostHandler),
webapp2.Route('/blog/<id:\d+>', PostPageHandler)
], debug=True)
