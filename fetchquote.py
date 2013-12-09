# accountLookp.py

import os

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler

class getquotefromtwitter(RequestHandler):
	def get(self):		
		news_rss_url = 'http://search.twitter.com/search.atom?q=perkytweets'
		import feedparser
		info = feedparser.parse(news_rss_url)
		records1 = ['anv']
		records2 = ['gwd']
		records3 = ['ldo']
		template_values1 = {"accounts1": records1, 'category1' : 'personal'};
		path = os.path.join(os.path.dirname(__file__), "templates/main.html")
		self.response.out.write(template.render(path, template_values1))

		template_values2 = {"accounts1": records2, 'category1' : 'finance '};
		path = os.path.join(os.path.dirname(__file__), "templates/main.html")
		self.response.out.write(template.render(path, template_values2))

		template_values3 = {"accounts1": records3, 'category1' : 'sports  '};
		path = os.path.join(os.path.dirname(__file__), "templates/main.html")
		self.response.out.write(template.render(path, template_values3))
