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
import webapp2

import os
import jinja2
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(autoescape=True,
                                       loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))


class Movie(ndb.Model):
    title = ndb.StringProperty()
    year = ndb.StringProperty()
    rated = ndb.StringProperty()
    # released = ndb.DateProperty()
    # runtime = ndb.StringProperty()
    # genre = ndb.StringProperty()
    director = ndb.StringProperty()
    # #actors = [ndb.StringProperty()]
    # # plot = ndb.StringProperty()
    # movieID = ndb.StringProperty()


# [END delete_entity]
class MainPage(webapp2.RequestHandler):





    def get(self):


        test = Movie()
        test.populate(
            title='The Departed',
            year='2006',
            rated='R',
            director="Martin Scorsese"
        )
        test.key = ndb.Key('Movie', test.director)

        test.put()
        testkey = test.key
        testid = testkey.id()
        template = jinja_environment.get_template('index.htm')

        updatekey = "Martin Scorsese"
        k = ndb.Key('Movie', updatekey)
        e = k.get()
        # print(e)
        e.director = "Steve Jobs"
        e.put()
        print(e)


        #retrieving works
        context = {
            'id': "222",
            'movieName': test.title,
            'yearReleased' : test.year,
            'movieRated' : test.rated,
            'directorName': test.director
        }
        print(testkey)






        deleteid = "Steve jobs"
        y = ndb.Key('Movie', deleteid)
        y.delete()
        print("deleting stuff")



        self.response.write(template.render(context))


    def post(self):
        test = Movie()
        test.title = self.request.get("title")
        test.year = self.request.get("year")
        test.rated = self.request.get("rated")
        test.director = self.request.get("director")
        test.key = ndb.Key('Movie', test.director)

        test.put()

application = webapp2.WSGIApplication([
    ('/',MainPage),
], debug=True)

