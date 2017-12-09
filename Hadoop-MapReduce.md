	
# MapReduce

6. Download Test Data

* 6.1 Download the Data File from Internet
	
	```
        #cd ~                   
        //command to go back to the home directory
	```
	```
        #mkdir test             
        //command to create new directory name test
	```
	```
        #cd test                
        //command to open the test directory
	```
	```
        #wget http://content.udacity-data.com/courses/ud617/purchases.txt.gz    
        //command to download the file from Internet
 	```
	
* 6.2 Extract the Data File

	```
        #gzip –d purchases.txt.gz
        //command to extract the file
 	```
	
* 6.3 Test the Data File
        
	```
        #head -10 purchases.txt
        //command to display the first 10 lines in file
	```
	
7. Edit the Mapper Function and Reducer Function

* 7.1 Edit Mapper Function
	
	```
	#vi mapper.py
	//command to open the mapper file
	```
	copy the code in the mapper file from github to local machine
 	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	
* 7.2 Edit Reducer Function

	```
	#vi mapper.py
	//command to open the mapper file
	```
	copy the code in the mapper file from github to local machine
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```

* 7.3 Give the permission to running the python file
	
	```
	#chmod u+x mapper.py reducer.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 7.4 Test the code in Master ContainerLinux

	```
	#head -50 purchases.txt | ./mapper.py | sort | ./reducer.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```

8. Running MapReduce in Hadoop

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
  
* 8.1 Upload the test file to Hadoop
	
	'hadoop fs -' is the basic command for Hadoop system
	```
	#hadoop fs -mkdir test
	//command create test directory in hadoop system 
	```
  	```
	#hadoop fs -cp purchases.txt test/purchases
	//command copy the file to 
  	```
* 8.2 Upload the mapper and reducer to Hadoop
	
	```
	#cd ~/test
	//command open the test directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input input/purchases.txt -output outputtest
	//command to do MapReduce in hadoop
	```
* 8.3 Check the result

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
  
9. Restart the Docker

	When you finish running task, you will close the terminal.
	Next time, if you want to do another job, you need to restart the docker
	
* 9.1 Check container status
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
	
* 9.2 Reattach contianer
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
  
* 9.3 Restart Hadoop in master container

	Then use the master container to restart Hadoop
	```
	#./start-hadoop.sh
	//Command to restart the Hadoop
  	```
	
* 9.4 Repeat the Step 6, 7 
	
