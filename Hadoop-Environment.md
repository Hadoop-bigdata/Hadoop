# Hadoop Enviroment

Before doing any steps list belowed, make sure we are in the master container in Docker.

3. Build Hadoop network

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
	$docker start 0f3ae72bcf3b
	//command to start the contianer
	```
	0f3ae72bcf3b is the address for the container, you can check it by command 
	
	```
	$docker ps –a
	```
	
* 3.3 Attach Contianer
	```
	$docker exec -ti hadoop-master bash
	//command to connect bash system for the slave1
	```
	```
	$docker exec -ti hadoop-slave1 bash
	//command to connect bash system for the slave1
	```
	```
	$docker exec -ti hadoop-slave2 bash
	//command to connect bash system for the slave2
	```

4. HDFS management

	Hadoop Filesystem has its own web for user to manage their file. In order to take the benefit of web management.

* 4.1 Update apt-get

	Due to the Hadoop image is out of date, we need to do some update before setting up the environment.
	
	```
	#apt-get update
 	//command to update the apt-get
	```
	
* 4.2 Install vim

	Vim is the editor for Linux System. 
	In the project, we need vim to edit the codes.
	
	```
	#apt-get install vim
	//command install vim
 	```
	
* 4.3 Set up Web HDFS management environment

	vi is the command for Linux system to create new file to edit the code
	
	```
	#cd /usr/local/hadoop/etc/hadoop/
 	//command to change directory
	```
	```
	#vi core-site.xml
	//command to open the xml file
	```
	type `i` to insert the command
	```
	//command to insert the code in vim
	```
	
	type `:wq` save the file and quit the vim file.
	```
	//command to save code and quie the vim
	```
	copy the code from the core-site.xml in github 
	
* 4.4 Restart Hadoop

	Before Restart the Hadoop, make sure you already close Hadoop, to close the Hadoop follow step in 2.6.
	
	```
	#./start-hadoop.sh
	//command to start running Hadoop
	```
	After restart Hadoop, you can connect browser which belongs to HDFS.
	
	Open the Browser http://localhost:50070/
	
	It will login to the Hadoop page
	
5. Install Anaconda

	Make sure you are in Hadoop-Master bash, if you are not in Hadoop-master bash, do the step 3.3.
	
* 5.1 Download Anacoda
	
   	```
   	#mkdir python
   	//command to create new directory for python
   	#cd python
   	//command to change directory
   	```
   	```
   	#wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
   	//command to download Anaconda package
   	```
* 5.2 Install Anaconda
	
	```
	#bash Anaconda3-5.0.1-Linux-x86_64.sh
	//command to install Anaconda
	```
	Press `Enter` key in keyboard until command line continue display
	```
	Do you accept the license terms? [yes|no]
	```
	choose `yes` 
	Then, press `Enter` key in keyboard until command line continue display
	```
	Do you wish the installer to prepend the Anaconda3 install location to PATH in your /root/.bashrc ? [yes|no]
	```
	choose `yes` 
	
	Then finish the installation
	
	```
	#source ~/.bashrc
	//command to restart the environment
	```

* 5.3 Creat Hadoop Image
	```
	#exit
	//command to get out of bash 
	```
	```
	$docker commit hadoop-master hadoop:python
	//command to create docker image based on hadoop master
	```
	
* 5.4 Set up Environment
	```
	$cd hadoop-cluster-docker
	//command to open hadoop-cluster-docker directory 
	```
	```
	$vi start-container.sh
	//command to set up environment
	```
	copy the file attach in start-container.sh file

	
* 5.5 Check the Environment
	
	```
	$conda list 
	//check conda package
	```
	```
	$jupyter notebook --no-browser --allow-root --ip=*
	//start jupyter notebook on local machine based docker
	```
	After type the command above, the command will show a line to your local machine
	```
	to login with a token:
	http://localhost:8888/?token=94d2a0a6140510faf292c7bb5eb56058cb6071e856e6e473
	```
	
	
	
4. Download Test Data

* 4.1 Download the Data File from Internet
	
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
	
* 4.2 Extract the Data File

	```
        #gzip –d purchases.txt.gz
        //command to extract the file
 	```
	
* 4.3 Test the Data File
        
	```
        #head -10 purchases.txt
        //command to display the first 10 lines in file
	```
	
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
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 5.4 Test the code in Master ContainerLinux

	```
	#head -50 purchases.txt | ./mapper.py | sort | ./reducer.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```


