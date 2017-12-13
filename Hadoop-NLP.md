# Nature Language Processing on Amazon Review
   
## 9. NLP on Hadoop 

* 9.1 Review Amazon Review Website  
        
   Website: 
   http://jmcauley.ucsd.edu/data/amazon/
    
   The link for amazon review file
   
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ 'filename' .json.gz
    
   File name is the file you want to download
   For example:
   Review Kindle store
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Kindle_Store_5.json.gz
    

* 9.2 Download Amazon Review file 
    
   Make sure you are in Hadoop-Master bash
   
   ```
   mkdir NLP
   //command to create new directory for Nature Language Process
   cd NLP
   //command to change directory
   ``` 
        
   ```
   wget http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Musical_Instruments_5.json.gz
   //command to download the file

	```
	
## 10. Edit the Map Function and Reduce Function

* 10.1 Edit Map Function
	
	```
	#vi map_NLP.py
	//command to open the mapper file
	```	
 	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the mapper file from github to local machine
	
* 10.2 Edit ReducE Function

	```
	#vi reduce_NLP.py
	//command to open the mapper file
	```
	```
	type i to insert the command
	add the command at the bottom of the core-site.xml file
	type command : wq save the file and quit the vim file.
	```
	copy the code in the reducer file from github to local machine
	
* 10.3 Give the permission to running the python file
	
	```
	#chmod u+x map_NLP.py reduce_NLP.py
	//command to give the permission to running the file
	```
	```
	#ls
 	//command to display all the file 
	```
	If the file has permission, it should be in green color
	
* 10.4 Test the code in Master Container Linux

	```
	#head -50 purchases.txt | ./map_NLP.py | sort | ./reduce_NLP.py
	//command to show the first 50 element in file and use mapper and reducer to get the result
	```


