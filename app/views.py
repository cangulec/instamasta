from app import app
from flask import render_template
import re
import csv
import os
import sys
from py2neo import authenticate, Graph
###########################################

@app.route('/selfie')
def selfie():
	filepath = os.path.join(os.path.dirname(__file__),'friendResults.csv')
	with open(filepath, 'rb') as f:
                reader = csv.reader(f)
		friends = list(reader)
	return render_template("selfie.html",title='Home',friends=friends)
###########################################
@app.route('/relationshipcount')
def relcount():
        from py2neo import authenticate, Graph
# set up authentication parameters
        authenticate("localhost:7474", "neo4j", "parola")
# connect to authenticated graph database
        graph = Graph("http://localhost:7474/db/data/")
        results = graph.cypher.execute("MATCH ()-[r]->() RETURN count(r)")
        return str(results)
###########################################
@app.route('/shortestpath/<n>/<j>')
def shortpath(n,j):
# set up authentication parameters
        authenticate("localhost:7474", "neo4j", "parola")
# connect to authenticated graph database
        graph = Graph("http://localhost:7474/db/data/")
        results = graph.cypher.execute("MATCH (martin:PERSON),(oliver:PERSON ),p = shortestPath((martin)-[*..15]-(oliver)) where martin.id= '"+j+"' and oliver.id= '"+n+"' RETURN p")
	return render_template("path.html",title='Home',relationship = results[0][0],node1=n,node2=j)
###########################################
@app.route('/dashboard/<n>')
def following2(n):
	authenticate("localhost:7474", "neo4j", "parola")
        graph = Graph("http://localhost:7474/db/data/")
        followingResults = graph.cypher.execute("MATCH (a)-[r:FOLLOWS]->(b) WHERE id(a)= "+n+" RETURN b")
        followingName = []
	for person in followingResults:
		cleanName = re.findall('"([^"]*)"', str(person[0]))
		cleanName[2] = str (int(cleanName[2]) - 1) 
		followingName.append(cleanName)
        followerResults = graph.cypher.execute("MATCH (a)-[r:FOLLOWS]->(b) WHERE id(b)= "+n+" RETURN a")
        followerName = []
        for person in followerResults:
                cleanName = re.findall('"([^"]*)"', str(person[0]))
                cleanName[2] = str (int(cleanName[2]) - 1)
		followerName.append(cleanName)
	thisUser = graph.cypher.execute("Match (joe) where id(joe)= "+n+" return joe")
	thisUserCleanName = re.findall('"([^"]*)"', str(thisUser[0][0]))
	userPostResult = graph.cypher.execute("MATCH (a)-[r:POSTED]->(b)<-[t:LIKES]-(q) WHERE id(a)="+n+"  RETURN b.Name,b.id ,count(t) ORDER BY count(t) DESC")
	userPosts = []
	for post in userPostResult:
		cleanName = re.findall('"([^"]*)"', str(post[0]))
		userPosts.append(userPostResult)
	recommendationsResult = graph.cypher.execute("MATCH (joe)-[:FOLLOWS*2..2]->(friend_of_friend) WHERE NOT (joe)-[:FOLLOWS]-(friend_of_friend) and friend_of_friend.id <> joe.id and id(joe) = "+n+" RETURN friend_of_friend.Name,friend_of_friend.Username,friend_of_friend.id,Count(*) ORDER BY COUNT(*) DESC , friend_of_friend.Name LIMIT 10")
	return render_template("index.html",
                        title='Home',
                        followings=followingName,
			followers=followerName,
			followingcount = len(followingName),
			followercount = len(followerName),
			thisUser = thisUserCleanName,
			posts=userPosts,
			recommendations = recommendationsResult)
###########################################
@app.route('/')
@app.route('/index')
def index():
	from py2neo import authenticate, Graph
# set up authentication parameters
        authenticate("localhost:7474", "neo4j", "parola")
# connect to authenticated graph database
        graph = Graph("http://localhost:7474/db/data/")
	personCount = graph.cypher.execute("MATCH (n:PERSON) RETURN count(n)")
        postCount = graph.cypher.execute("MATCH (n:POST) RETURN count(n)")
	personFormatted = "{:,}".format(personCount[0][0])
	return render_template("login.html",
                       		personCount = personCount[0][0],
				postCount = postCount[0][0],
				 title='Home')
###########################################
@app.route('/post/<p>')
def post(p):
        from py2neo import authenticate, Graph
# connect to authenticated graph database
        graph = Graph("http://localhost:7474/db/data/")
        postCount = graph.cypher.execute("MATCH (p:PERSON)-[:LIKES]->(n:POST) where n.id= \""+p+"\" RETURN n,p")
        likerName = []
        for liker in postCount:
                cleanName = re.findall('"([^"]*)"', str(liker[1]))
                cleanName[2] = str (int(cleanName[2]) - 1)
		likerName.append(cleanName)
        return render_template("post.html",
                                likername = likerName)
