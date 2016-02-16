from __future__ import print_function
from random import randint
import sys
import os
import time
from faker import Factory
fake = Factory.create()
start_time = time.time()
users = {}
sys.path = ['/Library/Python/2.7/site-packages'] + sys.path
import random
import string
from random import randint

userFile = open('users.txt','a+')
print ("id:ID(Person),:LABEL,Name,Username", file=userFile)
followFile = open('follows.txt','a+')
print (":START_ID(Person),:END_ID(Person),:TYPE", file=followFile)
postFile = open('posts.txt','a+')
print ("id:ID(Post),:LABEL,Name", file=postFile)
likesFile  = open('likes.txt','a+')
print (":START_ID(Person),:END_ID(Post),:TYPE", file=likesFile)


def createUsername(): # return Fibonacci series up to n
	random_letters = []
	for i in range(12):
		random_letter = random.choice(string.letters)
		random_letters.append(random_letter)
	return random_letters	
 
s = "";
usercount = 0
postcount = 0
likecount = 0
followcount= 0

for _ in range(0,1000000):
	username = s.join(createUsername())
	users.update({username :fake.name().replace("'", "")})  

for key in users:
	usercount = usercount + 1
	print (str(usercount)+",PERSON,"+users[key]+","+key, file=userFile)

tempcount = 0;
for key in users:
	tempcount = tempcount + 1
	randomizeFollow = randint(1,10)
	for i in range(randomizeFollow):
		followcount = followcount + 1
		randomone = str(randint(1,usercount))
		print (str(tempcount)+","+randomone.replace(" ", "")+",FOLLOWS", file=followFile)

for i in range(10000000):
	actions = ['newUser','newPost','newPost','newPost', 'newFollow','newFollow','newLike','newLike','newLike','newLike','newLike','newLike']
	action = random.choice(actions)
	if action == 'newUser':
		username = s.join(createUsername())
		usercount = usercount + 1
		print (str(usercount)+",PERSON,"+fake.name().replace("'", "")+","+username, file=userFile)
		randomizeFollow = randint(1,10)
		for i in range(randomizeFollow):
			followcount = followcount + 1
			print (str(usercount)+","+str(randint(1,usercount))+",FOLLOWS", file=followFile)
	elif action == 'newFollow':
		followcount = followcount + 1
		print (str(randint(1,usercount))+","+str(randint(1,usercount))+",FOLLOWS", file=followFile)
	elif action == 'newPost':
		postcount = postcount+1
		print (str(postcount)+",POST,POPO", file=postFile)
		print (str(randint(1,usercount))+","+str(postcount)+",POSTED", file=postRelFile)
		for i in range(randint(1,120)):
			print (str(randint(1,usercount))+","+str(str(postcount))+",LIKES", file=likesFile)
	elif action == 'newLike':
		print (str(randint(1,usercount))+","+str(randint(1,postcount))+",LIKES", file=likesFile)

print("--- %s seconds ---" % (time.time() - start_time))