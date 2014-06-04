import urllib2
import sys
import operator
import os
import re
import HTMLParser

def err(st):
	sys.stderr.write(st)
	sys.stderr.write(os.linesep)

def stdoe(st):
	sys.stderr.write(st)
	sys.stderr.write(os.linesep)
	sys.stdout.write(st)
	sys.stdout.write(os.linesep)


def geturl(st,agent=None):
	headers = { 'User-Agent' : agent }
	req = urllib2.Request(st, None, headers)
	html = urllib2.urlopen(req).read()
	return html	

def readtext(st):
	f = open(st)
	body = ""
	for line in f:
		body += line
	f.close()
	return body

def isnumber(st):
	try:
		float(st)
		return True
	except:
		return False

def getbetween2(body,start,end):
	"""
	Get all strings in between two strings.
	This should be the same as getbetween(), but
	this one looks more efficient!
	"""
	strs = re.findall( re.escape(start) + \
		"(.*?)" + \
		re.escape(end), \
		body, re.DOTALL)
	return strs

def getbetween(body,start,end):
	"""
	THIS FUNCTION IS DEPRECATED
	Get all strings in between two strings.
	"""
	strs = []
	while True:
		idx1 = body.find(start)
		x = body[ idx1+len(start):: ]
		idx2 = x.find(end)
		if idx1 == -1 or idx2 == -1:
			break
		strs.append( x[0:idx2] )
	
		body = x[idx2+len(end)::]
	
	return strs

def sortdict(dc, rev=False):
	"""Returns a sorted dictionary"""
	return sorted(dc.iteritems(), key=operator.itemgetter(1), reverse=rev)	

def sorttuple(tp, idx, rev=False):
	"""Returns a sorted tuple"""
	return sorted(tp, key=lambda x: x[idx], reverse=rev)

def removeall(st, remove):
	"""Removes all chosen characters from the string"""
	return "".join([x for x in st if x not in remove])


def striphtml(st,unescape=False):
	"""
	Strips all html from the string.
	Requires the BeautifulSoup library:
	sudo pip install BeautifulSoup
	"""
	from BeautifulSoup import BeautifulSoup
	res = BeautifulSoup(st).findAll(text=True)
	if unescape == True:
		for i in range(0, len(res)):
			res[i] = HTMLParser.HTMLParser().unescape(res[i])
	return res
