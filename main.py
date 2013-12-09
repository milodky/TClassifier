# main.py

import os
from GeoParser import *
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from fetchquote import getquotefromtwitter
import cgi
import webapp2
MAIN_PAGE_HTML = """\
    <html>
    <body>
    <p>
    <span class="title">Welcome to the Tweets Classifier Application</span>
    </p>
    <form action="/" method="post">
    <div><textarea name="content" rows="1" cols="60"></textarea></div>
    <p>
    <span class="title">If you input a location that doesn't exist, you'll get tweets randomly</span>
    </p>
    <div><input type="submit" value="search"></div>
    </form>
    </body>
    </html>
    """
class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class FetchData(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)
    
    def post(self):
        self.response.write(MAIN_PAGE_HTML)
        address = self.request.get('content')
        GP = GeoParser(address)
	GeoCode = GP.GetGeoCode()
	import TwitterRequestHandler

	OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
	CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
	token = (OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	TRHandler = TwitterRequestHandler.TwitterRequestHandler(token)
	result = TRHandler.MakeRequest(GeoCode)


	records1 = result['personal']
	records2 = result['finance']
	records3 = result['sports']
	template_values1 = {"accounts1": records1, 'category1' : 'personal'};
	path = os.path.join(os.path.dirname(__file__), "templates/main.html")
	self.response.out.write(template.render(path, template_values1))

	template_values2 = {"accounts1": records2, 'category1' : 'finance '};
	path = os.path.join(os.path.dirname(__file__), "templates/main.html")
	self.response.out.write(template.render(path, template_values2))

	template_values3 = {"accounts1": records3, 'category1' : 'sports  '};
	path = os.path.join(os.path.dirname(__file__), "templates/main.html")
	self.response.out.write(template.render(path, template_values3))

	"""
        self.response.write('<html><body>Results:<pre>')

        self.response.write(cgi.escape(abc))
        
        self.response.write('</pre></body></html>')
	"""

application = webapp2.WSGIApplication([
                                       #("/", MainPage),
                                      ("/", FetchData),
                                      ],
                                      debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
