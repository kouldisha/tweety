#!/usr/bin/python
# -*- coding: utf-8 -*-

import oauth2



def oauth_req(url, key, secret, http_method="GET", post_body='', http_headers=None):
	print('We have reached here')
	consumer = oauth2.Consumer(key='m5RCpSt9A4hmoXT0tGMOYyond', secret='l7SHdo6iZlbXx2MOs0LHRqA4DNN93Zkc9YjZgeKuw9kERhYqiU')
	token = oauth2.Token(key=key, secret=secret)
	print('We are going to make the client call now')
	client = oauth2.Client(consumer, token)
	
	resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
	print('We have gotten the content back!')
	print('The type of object the content is: '+type(content))
	return content
 

def main():
	hashtag = raw_input("Enter your hashtag here!")
	home_timeline = oauth_req( ('https://stream.twitter.com/1.1/statuses/filter.json?delimited=length&track='+hashtag),'2664846194-riw9aPNlfuErVJaV9sRnJAQPISUw6fO0JNBaUB6', 'uoMC6trAmqLDHy8zqtH1cvbQo9MmC9ezlxpBCq5rSzTyT')
	print(type(home_timeline))


if __name__ == "__main__": main()