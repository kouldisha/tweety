#!/usr/bin/python
# -*- coding: utf-8 -*-

import oauth2



def oauth_req(url, key, secret, http_method="GET", post_body='', http_headers=None):
	print('We have reached here')
	consumer = oauth2.Consumer(key='', secret='')
	token = oauth2.Token(key=key, secret=secret)
	print('We are going to make the client call now')
	client = oauth2.Client(consumer, token)
	
	resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
	print('We have gotten the content back!')
	print('The type of object the content is: '+type(content))
	return content
 

def main():
	hashtag = raw_input("Enter your hashtag here!")
	home_timeline = oauth_req( ('https://stream.twitter.com/1.1/statuses/filter.json?delimited=length&track='+hashtag),key, secret)
	print(type(home_timeline))


if __name__ == "__main__": main()