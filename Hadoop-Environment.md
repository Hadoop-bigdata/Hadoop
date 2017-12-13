# Hadoop Enviroment

Before doing any steps list belowed, make sure we are in the master container in Docker.

## 3. Build Hadoop network

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

## 4. HDFS management

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
	
## 5. Install Packages

* 5.0 confirm attach to the master

	Make sure you are attach to the Hadoop-Master, if you are not sure whether you are in it, please close all your terminal and open a new terminal again, and then print:
	```
	#docker attach hadoop-master
	//link to the hadoop master
   	```
	
* 5.1 Download Python3
	
   	```
   	#mkdir python
   	//command to create new directory for python
   	#cd python
   	//command to change directory
   	```
   	```
   	#apt install  python3-pip
   	//command to download Python package
   	```
	
	Press `Enter` key in keyboard until command line continue display
	```
	Do you want to continue? [Y/n] y
	```
	choose `yes`
	
	After installing python, check python environment
	```
	#python3
	//command to check the python running on your computer
	exit()
	//command to exit python
	```
	
* 5.2 Install pip, Numpy, Pandas, Sklearn, Scipy, Vadar
	
	5.2.1 Install pip
	
	pip is a package management system used to install and manage software packages written in Python. 
	reference https://en.wikipedia.org/wiki/Pip_(package_manager)
	```
	#wget https://bootstrap.pypa.io/get-pip.py
	//command to download get pip.py 
	# python get-pip.py
	//command to get-pip file
	```
	
	5.2.2 Install Numpy
	
	NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
	reference https://en.wikipedia.org/wiki/NumPy
	```
	#pip install numpy
	//command to install numpy
	```
	
	5.2.3 Install Panda
	Pandas is a software library written for the Python programming language for data manipulation and analysis.
	reference https://en.wikipedia.org/wiki/Pandas_(software)
	```
	#pip install panda
	//command to install panda
	```
	
	5.2.4 Install Sklearn
	Scikit-learn is a free software machine learning library for the Python programming language.
	reference https://en.wikipedia.org/wiki/Scikit-learn
	```
	#pip install Sklearn
	//command to install sklearn
	```
	
	5.2.5 Install Scipy
	SciPy is an open source Python library used for scientific computing and technical computing.
	reference https://en.wikipedia.org/wiki/SciPy
	```
	#pip install Scipy
	//command to install scipy
	```
	
	5.2.6 Install vader.sentiment
	VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 
	reference https://github.com/cjhutto/vaderSentiment
	```
	#pip install vaderSentiment
	//command to install vaderSentiment
	```
	
* 5.3 Install twython
	
	twython is an necessary package to do the NLP job for MapReduce, we should make sure all machines have install it.
	
	```
	#conda install  -c conda-forge twython
	//command download mrjob to local machine
	```
	
* 5.4 Creat Hadoop Image
	```
	#exit
	//command to get out of bash 
	```
	```
	$docker commit hadoop-master hadoop:python
	//command to create docker image based on hadoop master
	```
	
* 5.5 Set up Environment
	```
	$cd hadoop-cluster-docker
	//command to open hadoop-cluster-docker directory 
	```
	```
	$vi start-container.sh
	//command to set up environment
	```
	copy the file attach in start-container.sh file

	
* 5.6 Check the Environment
	
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
	Open Broswer with link above, after that you could edit the code in local machine
	
	
