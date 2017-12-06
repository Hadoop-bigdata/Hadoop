# Hadoop Tutorial

#### This report help people who has intesest to learn big data project and want to build Hadoop Distribute File System in Mac or Windonws.


In the report, we use Docker to set up the Hadoop Environment. After the installation, we build our database system based on the data file from Kaggle, Kaggle is the best website for data scientists. Then, we use MAPPER function and REDUCER function to extract the data in our database and download the file from our database. 


Apache Hadoop is a software framework written in Java to process the big data via a cluster of Distribute Filesystem. It works like the batch layer in Lambda Architecture. Hadoop Distribute File System and MapReduce will help Lambda Architecture to achieve data extraction and storage.


Hadoop Distribute File System (HDFS) is the default filesystem in Hadoop, it was designed as a distributed filesystem that provides high-throughput access to application data. In HDFS, the big data file will be split into fixed size small files and each file will be duplicate into multiple data node, and the name node keep track of file location. Due to big data file will be duplicate many times, it is good to adopt the human fault tolerance.


The project include: 

1. Install Docker
	
2. Install Hadoop Image in Docker
	
3. HDFS management

4. Download Test Data

5. Edit the Mapper Function and Reducer Function

6. Build Hadoop network

7. Running Mapper Reducer in Hadoop
	
8. Restart the Docker

