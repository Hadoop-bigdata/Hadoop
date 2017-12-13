## 3. Hadoop Network

From kiwenlau's image, he already built one master contianer and two slave contianers in Hadoop environment. 
Before running the MapReduce function, we need to open two slave containers
	
* 3.1 Open extra Terminals or Command Line

	For Mac:
	
	First, click on terminal, then click the shell on the top bar
	Then click new window, it will open one more terminal for your computer 
	Repeat the step open one more terminal
	
* 3.2 Check Container Status
	
	```
	$docker ps –a
	//command to list all container in your docker
	```
	How to know the which container is master or slave, check the port columns, it will give the information
	
	Check the status for each contianer
	
	If the status said: 
	
	' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	
	```
	$docker start hadoop-master
	//command to start the contianer
	```
	hadoop-master is the name for the container, you can check it by command 
	
	```
	$docker ps –a
	```
	check the status


## 4. Operation in Docker
	
* 4.1  Attach Container

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
	
* 4.2 Stop Container
	```
	$docker stop hadoop-master
	//command to stop for the master
	```
	```
	$docker stop hadoop-slave1
	//command to stop for the slave1
	```
	```
	$docker stop hadoop-slave2
	//command to stop for the slave2
	```

* 4.3 Start Container
	```
	$docker start hadoop-master
	//command to start for the msater
	```
	```
	$docker start hadoop-slave1
	//command to start for the slave1
	```
	```
	$docker start hadoop-slave2
	//command to start for the slave2
	```
  
* 4.4 Restart Hadoop in master container

	Then use the master container to restart Hadoop
	```
	#./start-hadoop.sh
	//Command to restart the Hadoop
  	```
