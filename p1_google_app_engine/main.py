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

# Import Libraries to access Movies class and Web Browser Structure

import P1_fresh_tomatoes
import P1_media

# Prepare app to work in Google App Engine
import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Create Movies instances.  Parameters are:
		## Title
		## Tagline
		## Movie Poster (URL of jpg)
		## Movie Trailer (YouTube URL)

		toy_story = P1_media.Movie("Toy Story",
	                        "A story of a boy and his toys that come to life",
	                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
		the_mask = P1_media.Movie("The Mask",
	                       "From Zero to Hero",
	                       "https://upload.wikimedia.org/wikipedia/en/4/4b/The_Mask_%28film%29_poster.jpg",
	                       "https://www.youtube.com/watch?v=hOqVRwGVUkA")
		gladiator = P1_media.Movie("Gladiator",
	                        "A Hero Will Rise",
	                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
	                        "https://www.youtube.com/watch?v=AxQajgTyLcM")

		# Create List of Movies
		movies = [toy_story, the_mask, gladiator]

		# Display movies in browser (Google App Engine)
		self.response.write(P1_fresh_tomatoes.open_movies_page(movies))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)