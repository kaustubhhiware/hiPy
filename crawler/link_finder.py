#from html.parser 
import HTMLParser
##try:
#    from urllib.parse import urlparse
#except ImportError:
##     from urlparse import urlparseere

##from urllib import urlparse
##import urllib

#from urlparse import urlparse
import urlparse

class LinkFinder(HTMLParser):

	def __init__(self):
		super().__init__()


	def handle_starttag(self,tag,attrs):
		print(tag)

	def error(self,message):
		pass


finder=LinkFinder()
finder.feed('<html><head><title>Test</head></title>'
			'<body><h1>Parse me!</h1></body></html>')