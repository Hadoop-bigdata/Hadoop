	
# MapReduce
#### MapReduce is the aims test the dataset we upload in Hadoop

7. Running Mapper Reducer in Hadoop

	Before doing any steps list below, make sure you are in the master container.
	Also you need to make sure you already open three teriminals, one for master, one for slave1 and one for slave2
	
	In master container type
 	 ```
	#cd ~
	//command go back home directory
 	 ```
  	```
	#cd test
	//command open the test directory
	```
  
* 7.1 Upload the test file to Hadoop
	
	'hadoop fs -' is the basic command for Hadoop system
	```
	#hadoop fs -mkdir test
	//command create test directory in hadoop system 
	```
  	```
	#hadoop fs -cp purchases.txt test/purchases
	//command copy the file to 
  	```
* 7.2 Upload the mapper and reducer to Hadoop
	
	```
	#cd ~/test
	//command open the test directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input input/purchases.txt -output outputtest
	//command to do MapReduce in hadoop
	```
* 7.3 Check the result

	```
	#hadoop fs -ls
	//command to display directory in Hadoop system
  	```
  	```
	#hadoop fs -ls outputtest
	//command to display outputtest directory in Hadoop system
  	```
  	```
	#hadoop fs -cat outputtest/part-00000
	//command to check result for MapReduce
	```
  
8. Restart the Docker

	When you finish running task, you will close the terminal.
	Next time, if you want to do another job, you need to restart the docker
	
* 8.1 Check container status
	Open the teriminal
	```
	$docker ps –a
	//command to list all container in your docker
	```
	check the status for each contianer
	if the status said: ' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	```
	$docker start 0f3ae72bcf3b
	//command to start the contianer
  	```
	0f3ae72bcf3b is the name for the container, you can check it by command $docker ps –a
	
* 8.2 Reattach contianer
	```
	$docker exec -ti hadoop-master bash
	//command to connect bash system for the master
  	```
  	```
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
  	```
  	```
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2
	```
  
8.3 Restart Hadoop in master container

	Then use the master container to restart Hadoop
	```
	#./start-hadoop.sh
	//Command to restart the Hadoop
  	```
	
8.4 Repeat the Step 6, 7 
	
