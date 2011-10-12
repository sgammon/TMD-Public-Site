#!/usr/bin/env python
# encoding: utf-8
"""
tmd.py

Author: Momentum Labs <momentum.io>
Created: 10/11/2011

Copyright (c) 2011 momentum.io. All rights reserved.
"""

import os

import logging

import webapp2 as webapp
from webapp2_extras import jinja2

from google.appengine.ext.webapp.util import run_wsgi_app

class TMDHandler(webapp.RequestHandler):
	
	@webapp.cached_property
	def jinja2(self):
		return jinja2.get_jinja2(app=self.app)
	
	def render(self, template, context={}, **kwargs):
		
		baseContext = {
			'link': self.url_for
		}
		
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				context[k] = v
		
		for k, v in baseContext.items():
			context[k] = v
			
		self.response.write(self.jinja2.render_template(template, **context))


class MainPage(TMDHandler):
	
	def get(self):
		
		self.render('home.html')
		

TMD = webapp.WSGIApplication([
	('/', MainPage)
])


def main():
	run_wsgi_app(TMD)


if __name__ == '__main__':
	main()

