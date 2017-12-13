# Nature Language Processing on Amazon Review
   
## 10. NLP on Hadoop 

* 10.1 Review Amazon Review Website  

   This dataset contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.
   
   Website: http://jmcauley.ucsd.edu/data/amazon/
    
   The link for amazon review file
   
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ 'filename' .json.gz
    
   File name is the file you want to download
   For example:
   Review Kindle store
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Kindle_Store_5.json.gz
    

* 10.2 Download Amazon Review file 
    
   Make sure you are in Hadoop-Master bash
   
   ```
   mkdir NLP
   //command to create new directory for Nature Language Process
   cd NLP
   //command to change directory
   ``` 
   For this project, we will use reviews_Movies_TV_5.json as our dataset.
   ```
   wget http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Movies_and_TV_5.json.gz
   //command to download the file
   ```
* 10.3 Extract the file

	```
	#gzip –d reviews_Movies_and_TV_5.json.gz
	//command to extract the file
	```
	
## 11. Edit the Map Function and Reduce Function

* 11.1 Edit Map Function

	```
	#vi map_NLP.py
	//command to open the map file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the reducer file from github to local machine
	
* 11.2 Edit Reduce Function

	```
	#vi reduce_NLP.py
	//command to open the reduce file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the reducer file from github to local machine
	
* 11.3 Give the permission to running the python file
	
	```
	#chmod u+x map_NLP.py reduce_NLP.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 11.4 Test the code in Master Container Linux

	```
	#head -50 reviews_Movies_and_TV_5.json | ./map_NLP.py | sort | ./reduce_NLP.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```
	
## 12. Running MapReduce_NLP in Hadoop

* 12.0 Check the location

	Before doing any steps list below, make sure you are in the master container.
	
	Also you need to make sure you already open three teriminals, one for master, one for slave1 and one for slave2
	
* 12.1 Upload the test file to Hadoop
	
	`hadoop fs -` is the basic command for Hadoop system
	```
	#hadoop fs -mkdir nlp
	//command to create nlp directory in hadoop system 
	```
	```
	#hadoop fs -cp reviews_Movies_and_TV_5.json nlp/reviews_Movies_and_TV_5.json
	//command to copy the file to 
  	```
	
* 12.2 Upload the map and reduce to Hadoop
	```
	#cd ~/nlp
	//command open the nlp directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map_nlp.py -reducer reduce_nlp.py -file map_nlp.py -file reduce_nlp.py -input input/reviews_Movies_and_TV_5.json -output outputtest1
	//command to do MapReduce in hadoop
	```
* 12.3 Check the result
	```
	#hadoop fs -ls
	//command to display directory in Hadoop system
  	```
  	```
	#hadoop fs -ls outputtest1
	//command to display outputtest directory in Hadoop system
  	```
  	```
	#hadoop fs -cat outputtest1/part-00000
	//command to check result for MapReduce
	```

