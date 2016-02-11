![Instamasta](https://github.com/cangulec/instamasta/blob/master/logo.png)
InstaMasta is a proof-of-concept Instagram explorer and photo analyzer.

InstaMasta provides summary analytics, friend recommendations and quantifies levels of self-absorption of any given user by applying computer vision technologies on the users photos. Technologies used in the application are Hadoop, HDFS, Spark, Neo4j, Flask, Bootstrap and Face Recognition with OpenCV libraries.
# Graphing social media activity 

The data pipeline is as follows:

* The data is generated using csvSim.py script and placed in hdfs
* pySpark parses the data to fit the format that is expected by neo4j-import tool
* neo4j-import tool pushes the data into the database
* Front-end uses Flask, and directly queries the database as information is needed

# Quantifying self-absorption

InstaMasta has a very naive approach to quantifying self-absorption. Once every photo of all the friends of the user is downloaded to the server, face_detect.py script goes through each picture and detects number of faces using a pre-trained haar cascade. Depending on the number of faces, the picture is then classified as:

* Social
* Selfie
* Artsy
