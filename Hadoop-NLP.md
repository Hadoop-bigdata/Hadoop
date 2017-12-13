# Nature Language Processing on Amazon Review
   
## 9 NLP on Hadoop 

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

* 9.3 Download the package

   9.3.1 Install Python3
   ```
   # apt install  python3-pip
   //command to installl python3
   ```
   
