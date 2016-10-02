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
    year = ndb.IntegerProperty()
    rated = ndb.StringProperty()
    director = ndb.StringProperty()

Movie1 = Movie(title='The Departed',year=2006,rated='R',director="Martin Scorsese")
Movie1.key =  ndb.Key('Movie', 'Action')
Movie1.put()
Movie2 = Movie(title='The Hero',year=2011,rated='R',director="Robert Hanson")
Movie2.key =  ndb.Key('Movie', 'Comedy')
Movie2.put()
Movie3 = Movie(title='The Zero',year=2016,rated='R',director="Tom Hank")
Movie3.key =  ndb.Key('Movie', 'Cartoon')
Movie3.put()
Movie4 = Movie(title='Hangover',year=2010,rated='R',director="Martin Joker")
Movie4.key =  ndb.Key('Movie', 'SciFi')
Movie4.put()
Movie5 = Movie(title='Jason Bourne',year=2016,rated='R',director="Joseph Scorsese")
Movie5.key =  ndb.Key('Movie', 'Animation')
Movie5.put()




class MainPage(webapp2.RequestHandler):

    def get(self):
        test = Movie()
        # test.populate(
        #     title='The Departed',
        #     year='2006',
        #     rated='R',
        #     director="Martin Scorsese"
        # )
        #
        # test.key = ndb.Key('Movie', test.director)
        # k = test.key
        # getID = k.id()
        #
        # test.put()
        # testkey = test.key
        # testid = testkey.id()
        template = jinja_environment.get_template('index.htm')

    # #updateing stuff
    #     updatekey = "Martin Scorsese"
    #     k = ndb.Key('Movie', updatekey)
    #     e = k.get()
    #     # print(e)
    #     e.director = "Steve Jobs"
    #     e.put()
    #     print(e)


        #retrieving works
        context = {
            'id': "222",
            'movieName': test.title,
            'yearReleased' : test.year,
            'movieRated' : test.rated,
            'directorName': test.director
        }
        q = ndb.Movie.query().filter(Movie.year == 2006)
        results = q.get()
        for entity in results:
            print(entity)





        deleteid = "Steve jobs"
        y = ndb.Key('Movie', deleteid)
        y.delete()
        print("deleting stuff")

        self.response.write(template.render(context))

        query = Movie.query(kind='Movie', order=('-timestamp',))

        results = [
            'Time: {timestamp} Addr: {user_ip}'.format(**x)
            for x in query.fetch(limit=10)]

        output = 'Last 10 visits:\n{}'.format('\n'.join(results))

    def update(self):
        temp = ndb.Key('Movie', 'Animation')
        x = temp.get()
        x.director = 'Sanjay Shrestha'
        x.put()

    def post(self):
        test = Movie()
        test.title = self.request.get("title")
        test.year = int(self.request.get("year"))
        test.rated = self.request.get("rated")
        test.director = self.request.get("director")
        test.key = ndb.Key('Movie', test.director)
        test.put()

application = webapp2.WSGIApplication([
    ('/',MainPage),
], debug=True)

