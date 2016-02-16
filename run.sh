python csvGenerate.py

hadoop dfs -put ~/user.txt /user/parsedUsers.csv 
hadoop dfs -put ~/posts.txt /user/parsedPosts.csv 
hadoop dfs -put ~/follows.txt /user/parsedFollows.csv 
hadoop dfs -put ~/likes.txt /user/parsedLikes.csv 

./bin/spark-submit --driver-memory 5g --packages com.databricks:spark-csv_2.10:1.1.0 pyspark.py

hadoop dfs -copyToLocal /user/parsedUsers.csv ~/user.txt
hadoop dfs -copyToLocal /user/parsedPosts.csv ~/posts.txt
hadoop dfs -copyToLocal /user/parsedFollows.csv ~/follows.txt
hadoop dfs -copyToLocal /user/parsedLikes.csv ~likes.txt

./neo4j/bin/neo4j-import --into /tmp/my-neo --nodes /home/ubuntu/user.txt  --nodes /home/ubuntu/posts.txt --relationships /home/ubuntu/follow.txt --relationships /home/ubuntu/likes.txt --relationships /home/ubuntu/postRel.txt
./neo4j/bin/neo4j start


