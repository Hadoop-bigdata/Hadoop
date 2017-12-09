# Hadoop-Installion 

1. Install Docker

* 1.1 Download Docker 
	
	
  	For Mac: https://www.docker.com/docker-mac
	
  	For Windows: https://www.docker.com/docker-windows
	
	
* 1.2 Install Docker on the local machine
	
* 1.3 Set up Docker Environment
	
	
	For Mac:
	
	First, click on Docker logo next to your time clock, then click on preferences.
	In the perferences, click on advanced. The Docker default environment CPUs is 2 and Memory is 2GB.
	
	For running the Hadoop, I update the CPUs to 4 and Memory to 6GB for my computer.
	However, the Docker preferences depends on your computer.
	The more Memory and CPUs you give to Docker, the faster running speed you have. 
	
	
2. Install Hadoop Image in Docker

	After install Docker on the local machine, you need to open the terminal (for mac) or command line (for Windows)

* 2.1 Install Hadoop Image
	
	```
 	$docker pull kiwenlau/hadoop:1.0
	//command to pull Hadoop image into Docker
	```
	Thanks to kiwenlau who already build the Hadoop image in docker.
	
	Reference: https://github.com/kiwenlau/hadoop-cluster-docker
	
	In project, we will use his image to do MapReduce funtion. 
	
	
* 2.2 Create clone storage
	
	```
	$git clone https://github.com/kiwenlau/hadoop-cluster-docker
	```
	For the Mac users, if you meet the error
	```
	xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at : /Library/Developer/CommandLineTools/usr/bin/xcrun
	```
	You can try:
	```
	$xcode-select –install
	//command to download the xcode
	```
	After try download the xcode, then tyep the same code:
	```
	$git clone https://github.com/kiwenlau/hadoop-cluster-docker
 	```
* 2.3 Connect the Internet

	```
	$docker network create --driver=bridge Hadoop
 	//command to connect the master container with slave container
	```
	
* 2.4 Running the Master Container

	```
	$cd hadoop-cluster-docker
	//command 
	```
	```
	$./start-container.sh
	//command to start the container
 	```
	When you type the command, you are in the Linux system, which located in Docker container xxxx
	Also xxx is in the master container
	
* 2.5 Run the Hadoop in Docker
	
	```
	#./start-hadoop.sh
	//command to run the Hadoop in the container
 	```
* 2.6 Stop the Hadoop in Docker
	
	```
	#stop-all.sh
	//command to stop the Hadoop in the container,
	```
	
3. HDFS management

	Hadoop Filesystem has its own web for user to manage their file. In order to take the benefit of web management.
	We will set up this environment in step 2.

* 3.1 Update apt-get

	Due to the Hadoop image is out of date, we need to do some update before setting up the environment.
	
	```
	#apt-get update
 	//command to update the apt-get
	```
	
* 3.2 Install vim

	Vim is the editor for Linux System. 
	In the project, we need vim to edit the codes.
	
	```
	#apt-get install vim
	//command install vim
 	```
	
* 3.3 Set up Web HDFS management environment

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
	i
	//command to insert the code in vim
	```
	
	type `:wq` save the file and quit the vim file.
	```
	wq
	//command to save code and quie the vim
	```
	copy the code in the core-site.xml file
	
* 3.4 Restart Hadoop

	Before Restart the Hadoop, make sure you already close Hadoop, to close the Hadoop follow step in 2.6.
	
	```
	#./start-hadoop.sh
	//command to start running Hadoop
	```
	After restart Hadoop, you can connect browser which belongs to HDFS.
	Open the Browser http://localhost:50070/
	It will login to the Hadoop page
	
