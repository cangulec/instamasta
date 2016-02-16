from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict
import requests
import json
import os
start_time = time.time()

def getListofUsers(id,type,token):
	count = 0
	json = None
	url= "https://api.instagram.com/v1/users/"+id+"/"+type+"followed-by?access_token="+token
	while json is None or json.has_key('error_type'):
		try:
			json = requests.get(url).json()
			if not(json.has_key('data')):
				print "Hit API limit"
				print json
				time.sleep(100)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			print "Sleeping 5 sc"
			time.sleep(5)
	followers = []
	while json.has_key('pagination') and json['pagination'].has_key('next_url') and count < 2000:
		for user in json['data']:
			count = count + 1
			followers.append({'Username':user['username'],'Id':user['id']})
		nextpage = json['pagination']['next_url']
		json = None
		while json is None or json.has_key('error_type'):
			try:
				json = requests.get(nextpage).json()
				if not(json.has_key('data')):
					print "Hit API limit"
					time.sleep(100)
			except:
				print "Sleeping 5 sc"
				time.sleep(5)
	if json.has_key('data'):
		for user in json['data']:
			followers.append({'Username':user['username'],'Id':user['id']})

	return followers
			

## INPUT ACCSESS TOKEN HERE
access_token = "XXXXXXXXXXXXXXXXXXXXXXX"

f = open('canScrape.txt','a+')
j = open('jsonLOG.txt','a+')
following =  getFollowing('self','follows',access_token)

print "Finished initilializing"

for user in following:
	f.write("185381657,cangulec,FOLLOWS,"+user['Username']+","+user['Id']+"\n")
	userFollows =  getListofUsers(user['Id'],'follows',access_token)
	for userfollow in userFollows:
		f.write(user['Id']+","+user['Username']+",FOLLOWS,"+userfollow['Username']+","+userfollow['Id']+"\n")
	userFollows =  getListofUsers(user['Id'],'followed-by',access_token)
	for userfollowedby in userFollows:
		f.write(userfollowedby['Id']+","+userfollowedby['Username']+",FOLLOWS,"+user['Username']+","+user['Id']+"\n")
	print user['Username']
	print 'Done'
	
print("--- %s seconds ---" % (time.time() - start_time))

   		
   







