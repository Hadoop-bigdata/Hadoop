# Enviroment

Before doing any steps list belowed, make sure we are in the master container in Docker.

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
	

	
## 6. Install Packages

* 6.0 confirm attach to the master

	Make sure you are attach to the Hadoop-Master, if you are not sure whether you are in it, please close all your terminal and open a new terminal again, and then print:
	```
	#docker attach hadoop-master
	//command to link to the hadoop master
   	```
	
* 5.1 Update apt-get

	Due to the Hadoop image is out of date, we need to do some update before setting up the environment.
	```
	#apt-get update
 	//command to update the apt-get
	```
	
* 5.2 Install vim

	Vim is the editor for Linux System. 
	In the project, we need vim to edit the codes.
	```
	#apt-get install vim
	//command to install vim
 	```
	
* 6.1 Download Python3
	
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
	
* 6.2 Install pip, Numpy, Pandas, Sklearn, Scipy, Vadar
	
	6.2.1 Install pip
	
	pip is a package management system used to install and manage software packages written in Python. 
	
	Reference https://en.wikipedia.org/wiki/Pip_(package_manager)
	```
	#wget https://bootstrap.pypa.io/get-pip.py
	//command to download get pip.py 
	# python get-pip.py
	//command to get-pip file
	```
	
	6.2.2 Install Numpy
	
	NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
	
	Reference https://en.wikipedia.org/wiki/NumPy
	```
	#pip install numpy
	//command to install numpy
	```
	
	6.2.3 Install Pandas
	
	Pandas is a software library written for the Python programming language for data manipulation and analysis.
	
	Reference https://en.wikipedia.org/wiki/Pandas_(software)
	```
	#pip install panda
	//command to install pandas
	```
	
	6.2.4 Install Sklearn
	
	Scikit-learn is a free software machine learning library for the Python programming language.
	
	Reference https://en.wikipedia.org/wiki/Scikit-learn
	```
	#pip install Sklearn
	//command to install sklearn
	```
	
	6.2.5 Install Scipy
	
	SciPy is an open source Python library used for scientific computing and technical computing.
	
	Reference https://en.wikipedia.org/wiki/SciPy
	```
	#pip install Scipy
	//command to install scipy
	```
	
	6.2.6 Install vader.sentiment
	
	VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 
	
	Reference https://github.com/cjhutto/vaderSentiment
	```
	#pip install vaderSentiment
	//command to install vaderSentiment
	```
	
* 6.3 Creat Hadoop Image
	```
	#exit
	//command to get out of bash 
	```
	```
	$docker commit hadoop-master hadoop:python
	//command to create docker image based on hadoop master
	```
	
* 6.4 Restart Hadoop container
	```
	$cd hadoop-cluster-docker
	//command to find the hadoop file
	$ vi start-container.sh
	//change the file content
	```
	copy the file start-container.sh
	
