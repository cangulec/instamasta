![Instamasta](https://github.com/cangulec/instamasta/blob/master/logo.png)
InstaMasta is a proof-of-concept Instagram explorer and photo analyzer.

InstaMasta provides summary analytics, friend recommendations and quantifies levels of self-absorption of any given user by applying computer vision technologies on the users photos. Technologies used in the application are Hadoop, HDFS, Spark, Neo4j, Flask, Bootstrap and Face Recognition with OpenCV libraries.
# Graphing social media activity 

InstaMasta uses Neo4j as its primary database. The data pipeline is as follows:

* The data is generated using csvSim.py script and placed in hdfs
* pySpark parses the data to fit the format that is expected by neo4j-import tool
* neo4j-import tool pushes the data into the database
* Front-end uses Flask, and directly queries the database as information is needed

# Quantifying self-absorption
