# 

1. Instal Anaconda
   
   Make sure you are in Hadoop-Master bash
   ```
   mkdir python
   //command to create new directory for python
   cd python
   //command to change directory
   ```
   ```
   wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
   //command to download Anaconda package
   ```
   
   
1. Review Amazon Review Website  
        
   Website: 
   http://jmcauley.ucsd.edu/data/amazon/
    
   The link for amazon review file
   
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ 'filename' .json.gz
    
   File name is the file you want to download
   For example:
   Review Kindle store
   http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Kindle_Store_5.json.gz
    

2. Download Amazon Review file 
    
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
