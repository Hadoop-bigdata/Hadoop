1 Install Docker

	1.1 Download Docker 
  	For Mac: https://www.docker.com/docker-mac
  	For Windows: https://www.docker.com/docker-windows
	
	1.2 Install Docker on the local machine
	
	1.3 Set up Docker Environment
	For Mac:
	First, click on Docker logo next to your time clock, then click on preferences.
	In the perferences, click on advanced. The Docker default environment CPUs is 2 and Memory is 2GB. 
	For running the Hadoop, I update the CPUs to 4 and Memory to 6GB for my computer.
	However, the Docker preferences depends on your computer.
	The more Memory and CPUs you give to Docker, the faster running speed you have. 

2 Install Hadoop Image in Docker
After install Docker on the local machine, you need to open the terminal (for mac) or command line (for Windows)

	2.1 Install Hadoop Image

 	$docker pull kiwenlau/hadoop:1.0
	//command pull Hadoop image into Docker
	Thanks to kiwenlau who already build the Hadoop image in docker.
	In our project, we will use his image to do projects  
	
	2.2 Create clone storage
	
	$git clone https://github.com/kiwenlau/hadoop-cluster-docker
	
	For the Mac users, if you meet the error
	
	You can try:
	
	$xcode-select –install
	//command download the xcode
	
	After try download the xcode, then tyep the same code:
	$git clone https://github.com/kiwenlau/hadoop-cluster-docker
 
	2.3 Connect the Internet

	$docker network create --driver=bridge Hadoop
 	//command connect the master container with slave container
	
	2.4 Running the Master Container

	$cd hadoop-cluster-docker
	//command 
	$./start-container.sh
	//command to start the container
 
	When you type the command, you are in the Linux system, which located in Docker container xxxx
	Also xxx is in the master container
	
	2.5 Run the Hadoop in Docker
	
	#./start-hadoop.sh
	//command to run the Hadoop in the container
 
	2.6 Stop the Hadoop in Docker
	
	#stop-all.sh
	//command to stop the Hadoop in the container,
	
3 HDFS management
Hadoop Filesystem has its own web for user to manage their file. In order to take the benefit of web management.
We will set up this environment in step 2.

	3.1 Update apt-get
	Due to the Hadoop image is out of date, we need to do some update before setting up the environment.
	
	#apt-get update
 	//command to update the apt-get
	
	3.2 Install vim
	Vim is the editor for Linux System. 
	In the project, we need vim to edit the codes.
	
	#apt-get install vim
	//command install vim
 
	3.3 Set up Web HDFS management environment
	vi is the command for Linux system to create new file to edit the code
	
	#cd /usr/local/hadoop/etc/hadoop/
 	//command to change directory
	#vi core-site.xml
	//command to open the xml file
	
	‘’’
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : and the type wq save the file and quit the vim file.
	‘’’
	copy the code in the core-site.xml file
	
	3.4 Restart Hadoop
	Before Restart the Hadoop, make sure you already close Hadoop, to close the Hadoop follow step in 2.6.
	
	#./start-hadoop.sh
	After restart Hadoop, you can connect browser which belongs to HDFS.
	Open the Browser http://localhost:50070/
	It will login to the Hadoop page

4. Download Test Data
Before doing any steps list belowed, make sure we are in the master container in Docker.

	4.1 Download the Data File from Internet

        #cd ~                   
        //command go back to the home directory
        #mkdir test             
        //command create new directory name test
        #cd test                
        //command open the test directory                
        #wget http://content.udacity-data.com/courses/ud617/purchases.txt.gz    
        //commanddownload the file from Internet
 
	4.2 Extract the Data File

        #gzip –d purchases.txt.gz
        //command extract the file
 
	4.3 Test the Data File
        
        #head -10 purchases.txt
        //command display the first 10 lines in file

5 Edit the Mapper Function and Reducer Function
Before doing any steps list belowed, make sure we are in the master container in Docker.

	5.1 Edit Mapper Function
	
	#vi mapper.py
	//command to open the mapper file
	
	copy the code in the mapper file from github to local machine
 	‘’’
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	‘’’
	
	5.2 Edit Reducer Function
	#vi mapper.py
	//command to open the mapper file
	
	copy the code in the mapper file from github to local machine
	‘’’
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	‘’’

	5.3 Give the permission to running the python file
	
	#chmod u+x mapper.py reducer.py
	//command give the permission to running the file 
	#ls
 	//display the file 
	If the file has permission, it should be in green color
	
	5.4 Test the code in Master ContainerLinux
	
	#head -50 purchases.txt | ./mapper.py | sort | ./reducer.py
	//command show the first 50 element in file and use mapper and reducer to get the result

6 Build Hadoop network
From kiwenlau's image, he already built one master contianer and two slave contianers in Hadoop environment. 
Before running the MapReduce function, we need to open two slave containers

	6.1 Open extract temriminals or command line
	For Mac:
	First, click on terminal, then click the shell on the top bar
	Then click new window, it will open one more terminal for your computer 
	Repeat the step open one more terminal
	
	6.1 Check container status

	$docker ps –a
	//command to list all container in your docker
	How to know the which container is master or slave, check the port columns, it will give the information
	
	check the status for each contianer
	if the status said: ' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	
		$docker start 0f3ae72bcf3b
		//command to start the contianer
		0f3ae72bcf3b is the name for the container, you can check it by command $docker ps –a
	 
	6.2 Attach slave contianer
	
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2

7 Running Mapper Reducer in Hadoop
Before doing any steps list below, make sure you are in the master container.
Also you need to make sure you already open three teriminals, one for master, one for slave1 and one for slave2
	
	In master container type
	#cd ~
	//command go back home directory
	#cd test
	//command open the test directory
	
	7.1 Upload the test file to Hadoop
	
	'hadoop fs -' is the basic command for Hadoop system
	
	#hadoop fs -mkdir test
	//command create test directory in hadoop system 
	
	#hadoop fs -cp purchases.txt test/purchases
	//command copy the file to 
 
	7.2 Upload the mapper and reducer to Hadoop
	
	#cd ~/test
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input input/purchases.txt -output outputtest
	//command to do MapReduce in hadoop
	
	7.3 Check the result
	
	#hadoop fs -ls
	//command to display directory in Hadoop system
	#hadoop fs -ls outputtest
	//command to display outputtest directory in Hadoop system
	#hadoop fs -cat outputtest/part-00000
	//command to check result for MapReduce
	
8 Restart the Docker
When you finish running task, you will close the terminal.
Next time, if you want to do another job, you need to restart the docker
	
	8.1 Check container status
	Open the teriminal
	
	$docker ps –a
	//command to list all container in your docker
	
	check the status for each contianer
	if the status said: ' Exited (137) xx minutes(hours) ago' means the container is stop, you need to restart the container
	
		$docker start 0f3ae72bcf3b
		//command to start the contianer
		0f3ae72bcf3b is the name for the container, you can check it by command $docker ps –a
	
	8.2 Reattach contianer
	
	$docker exec -ti hadoop-master bash
	//command to connect bash system for the master
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2
	
	8.3 Restart Hadoop in master container
	Then use the master container to restart Hadoop
	
	#./start-hadoop.sh
	//Command to restart the Hadoop
	
	8.4 Repeat the Step 6, 7 
	
