#!/usr/bin/env python
import time,string
import urllib,urllib2,cookielib
from random import randint,choice  


def readconf(mylist,filename):
	conf = open(filename,"rb")
	for lines in conf:
		item = lines.rstrip("\r\n")
		mylist.append(item)
	conf.close

def main():
	firstnames = []
	readconf(firstnames,'firstnames.txt')
	conchar = ['.','_']
	surnames = []
	readconf(surnames,'surnames.txt')
	doms = []
	readconf(doms,'doms.txt')
	email = choice(firstnames) + choice(conchar) + choice(surnames) + '@' + choice(doms)
	print email
	myCookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
	openner = urllib2.build_opener(myCookie)
	# this should be the <input name='vote[email]'> in the page
	post_data = {'vote[email]':email,'vote[entry_id]':'115'}
	#should match  <form method="post" id="voteform" name="vote" action="http://www.cenovis.com.au/win-the-goods-entry/index.php/enter/detail" >
	req = urllib2.Request('http://www.cenovis.com.au/win-the-goods-entry/index.php/enter/detail', urllib.urlencode(post_data))
	html_src = openner.open(req).read()
	result = open("voted.log","a")
	result.write(email+"\n")
	result.close()

if __name__ == "__main__":
    	main()





