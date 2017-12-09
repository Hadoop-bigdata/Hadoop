# Hadoop Tutorial

#### This reports helps people who has intesest to learn big data project and want to build Hadoop Distribute File System within Mac or Windonws system.


In the report, we use Docker to set up the Hadoop Environment. After the installation, we build our database system based on the data file from Kaggle, Kaggle is the one of the best websites for data scientists. Then, we use MAPPER function and REDUCER function to extract the data in our database and download the file from our database. 


Apache Hadoop is a software framework written in Java to process the big data via a cluster of Distribute Filesystem. It works like the batch layer in Lambda Architecture. Hadoop Distribute File System and MapReduce will help Lambda Architecture to achieve data extraction and storage.


Hadoop Distribute File System (HDFS) is the default filesystem in Hadoop, it was designed as a distributed filesystem that provides high-throughput access to application data. In HDFS, the big data file will be split into fixed size small files and each file will be duplicate into multiple datanode, and the namenode keeps track of file location. Due to big data file will be duplicated many times, it is good to adopt the human fault tolerance.


#### The project include: 

#### First part: Installation
```
1. Install Docker
	
2. Install Hadoop Image in Docker
```

#### Second part: Setting up Environment
```
3. HDFS management

4. Download Test Data

5. Edit the Mapper Function and Reducer Function
```
#### Third part: Test Hadoop Distribute File System 
```
6. Build Hadoop network

7. Running Mapper Reducer in Hadoop
	
8. Restart the Docker
```

#### Fourth part: Nature Language Processing on Amazon Review
```
9. Download the Amazon Review
```


