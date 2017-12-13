	
# MapReduce on Test Data set

## 4. Download Test Data

* 4.1 Download the Test Data File from Internet

	```
	#cd ~                   
	//command to go back to the home directory
	#mkdir test             
	//command to create new directory name test
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
	
## 5. Edit the Map Function and Reduce Function

* 5.1 Edit Map Function
	
	```
	#vi map.py
	//command to open the map file
	```	
 	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the map.py
	
* 5.2 Edit Reduce Function

	```
	#vi reduce.py
	//command to open the reduce file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the reduce.py
	
* 5.3 Give the permission to running the python file
	
	```
	#chmod u+x map.py reduce.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 5.4 Test the code in Master Container Linux

	```
	#head n -50 purchases.txt | ./map.py | sort | ./reduce.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```

## 6. Running MapReduce in Hadoop

* 6.1 Check the location

	Before doing any steps list below, make sure you are in the master container.
	Also you need to make sure you already open three teriminals, one for master, one for slave1 and one for slave2
	```
	#cd ~
	//command to go back home directory
	#./start-hadoop.sh
	//command start hadoop
	```
	In master container type
	```
	#cd ~
	//command go back home directory
	```
	```
	#cd test
	//command open the test directory
	```
  
* 6.2 Upload the test file to Hadoop
	
	`hadoop fs -` is the basic command for Hadoop system
  	```
	#hadoop fs -put purchases.txt input/purchases
	//command put the file to hadoop
  	```
* 6.3 Upload the map and reduce to Hadoop
	```
	#cd ~/test
	//command open the test directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map.py -reducer reduce.py -file map.py -file reduce.py -input input/purchases.txt -output outputtest
	//command to do MapReduce in hadoop
	```
* 6.4 Check the result
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
  

	
