from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName = "MyApp")
sqlContext = SQLContext(sc)

fileUser = "hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/users.csv"
filePost = "hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/posts.csv"
fileFollows = "hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/follows.csv"
fileLikes = "hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/likes.csv"

dfUser = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(fileUser)
dfUser.select('Id','Type','Username').write.format('com.databricks.spark.csv').save('hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/parsedUsers.csv')

dfPost = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(filePost)
dfPost.select('Id','Type','Username').write.format('com.databricks.spark.csv').save('hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/parsedPosts.csv')

dfFollows = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(fileFollows)
dfFollows.select('From','Type','To').write.format('com.databricks.spark.csv').save('hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/parsedFollows.csv')

dfLikes = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(fileFollows)
dfLikes.select('From','Type','To').write.format('com.databricks.spark.csv').save('hdfs://ec2-52-6-165-80.compute-1.amazonaws.com:9000/user/parsedLikes.csv')
