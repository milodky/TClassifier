import os,urllib

class GeoParser(object):
	def __init__(self, addr):
		self.url = 'http://maps.google.com/?q=' + urllib.quote(addr) + '&output=js'
	def GetGeoCode(self):
		xml = urllib.urlopen(self.url).read()
		if '<error>' in xml:
			return 'Invalid'
		else:
			lat,lng = 0.0,0.0
			center = xml[xml.find('{center')+10:xml.find('}',xml.find('{center'))]
			GeoCode = center.replace('at:','').replace('lng:','')
			return GeoCode
