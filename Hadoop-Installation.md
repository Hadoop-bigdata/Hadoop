# Hadoop-Installation

## 1. Install Docker

* 1.1 Download Docker 
	
	Before Download the Docker make sure your computer will support vitrual machine.

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
	
## 2. Install Hadoop Image in Docker

After install Docker on the local machine, you need to open the terminal (for mac) or command line (for Windows)
	
* 2.1 Install Hadoop Image
	
	```
	$docker pull kiwenlau/hadoop:1.0
	//command to pull Hadoop image into Docker
	```
	Thanks to kiwenlau who already build the Hadoop image in docker.
	
	Reference: https://github.com/kiwenlau/hadoop-cluster-docker
	
	In project, we will use his Hadoop image to do Project. 
	
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

