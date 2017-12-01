# Hadoop Test
#### Haddop Test use the file downlod from Internet to test the Hadoop Environmental

Follow the step in Hadoop-Install

Before doing any steps list belowed, make sure we are in the master container in Docker.

4. Download Test Data

* 4.1 Download the Data File from Internet

        #cd ~                   
        //command go back to the home directory
        #mkdir test             
        //command create new directory name test
        #cd test                
        //command open the test directory                
        #wget http://content.udacity-data.com/courses/ud617/purchases.txt.gz    
        //commanddownload the file from Internet
 
* 4.2 Extract the Data File

        #gzip –d purchases.txt.gz
        //command extract the file
 
* 4.3 Test the Data File
        
        #head -10 purchases.txt
        //command display the first 10 lines in file

5. Edit the Mapper Function and Reducer Function

* 5.1 Edit Mapper Function
	
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
	
* 5.2 Edit Reducer Function

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

* 5.3 Give the permission to running the python file
	
	```
	#chmod u+x mapper.py reducer.py
	//command give the permission to running the file 
	#ls
 	//display the file 
	```
	If the file has permission, it should be in green color
	
* 5.4 Test the code in Master ContainerLinux

	```
	#head -50 purchases.txt | ./mapper.py | sort | ./reducer.py
	//command show the first 50 element in file and use mapper and reducer to get the result
	```
6. Build Hadoop network

	From kiwenlau's image, he already built one master contianer and two slave contianers in Hadoop environment. 
	Before running the MapReduce function, we need to open two slave containers
	
* 6.1 Open extract temriminals or command line

	For Mac:
	```
	First, click on terminal, then click the shell on the top bar
	Then click new window, it will open one more terminal for your computer 
	Repeat the step open one more terminal
	```
* 6.2 Check container status
	
	```
	$docker ps –a
	//command to list all container in your docker
	```
	How to know the which container is master or slave, check the port columns, it will give the information
	
	check the status for each contianer
	
	if the status said: ' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	
	```
	$docker start 0f3ae72bcf3b
	//command to start the contianer
	```
	0f3ae72bcf3b is the name for the container, you can check it by command $docker ps –a
	 
* 6.3 Attach slave contianer
	
	```
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2
	```

