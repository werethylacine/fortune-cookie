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

# fortune-cookie favicon from: http://www.favicon.cc/?action=icon&file_id=65239

import webapp2
import random

def fortuneTeller():
    fortunes = [
        "You're about to find belly-button lint!",
        "Someone you know has a crush on you.",
        "Someone you know is actually a dragon."
    ]
    idx = random.randrange(len(fortunes))
    return fortunes[idx]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        lucky_num = str(random.randrange(10))
        style = '<head><link type="text/css" rel="stylesheet" href="/stylesheets/fortune_styles.css" /></head>'
        buttn = '<p><button><a href = "."> Open another cookie </a></button></p>'
        self.response.write(style + '<body><p style = "color:red"> &#9786 ' + fortuneTeller() + ' &#9786</p><p> Your lucky number is: ' + lucky_num + '</p>' + buttn + '</body>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
