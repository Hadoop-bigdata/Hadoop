# Nature Language Processing on Amazon Review
   
## 7. Download Amazon Review 

* 7.1 Review Amazon Review Website  

   This dataset contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.
   
   Website: http://jmcauley.ucsd.edu/data/amazon/
    
   The link for amazon review file
   
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ 'filename' .json.gz
    
   File name is the file you want to download
   For example:
   Review Kindle store
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Kindle_Store_5.json.gz
    

* 7.2 Download Amazon Review file 
    
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
   
* 7.3 Extract the file

	```
	#gzip -d reviews_Movies_and_TV_5.json.gz 
	//command to extract the file
	```
	
## 8. Edit the Map Function and Reduce Function

* 8.1 Edit Map Function

	```
	#vi map_NLP.py
	//command to open the map file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the map_NLP.py
	
* 8.2 Edit Reduce Function

	```
	#vi reduce_NLP.py
	//command to open the reduce file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the reduce_NLP.py
	
* 8.3 Give the permission to running the python file
	
	```
	#chmod u+x map_NLP.py reduce_NLP.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 8.4 Test the code in Master Container Linux

	```
	#head -n 100 reviews_Movies_and_TV_5.json | ./map_NLP.py | sort | ./reduce_NLP.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```
	Check the `n value` in reduce_NLP.py.
	
	In order to run the test code, the command head -n `number` the number should be bigger than the n value in the reduce_NLP.py 
	
	
## 9. Running MapReduce_NLP in Hadoop

After change the test, we need to replace the n back to the default value.

* 9.1 Check the location

	```
	cd ~/NLP
	//command to change the directory
	```
	
* 9.2 Upload the test file to Hadoop
	
	`hadoop fs -` is the basic command for Hadoop system
	```
	#hadoop fs -put reviews_Movies_and_TV_5.json input/
	//command to input the file to hadoop 
  	```
	
* 9.3 Upload the map and reduce to Hadoop
	```
	#cd ~/nlp
	//command to open the nlp directory
	```
	```
	#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper map_NLP.py -reducer reduce_NLP.py -file map_NLP.py -file reduce_NLP.py -input input/reviews_Movies_and_TV_5.json -output outputtest1
	//command to do MapReduce in hadoop
	```
* 9.4 Check the result
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

