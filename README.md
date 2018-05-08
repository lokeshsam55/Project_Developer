# Project_Developer
The Objective of this project was to read a file from local disk and write to a message system using Kafka and application that reads data from the message system and detects whether the attacker is part of the DDOS attack and once an attacker is found, the ip-address should be written to a results directory which could be used for further processing.

### Prerequisite

1. Kafka_2.11-1.0.0

Link: https://kafka.apache.org/downloads

2. Python 2.7

Link: https://www.python.org/ftp/python/2.7.15/

3. spark-2.2.1-bin-hadoop2.7

Link: https://spark.apache.org/downloads.html

###  Apache Log Format
84.56.41.58 - - [18/Apr/2016:06:52:07 +0100] "GET /wordpress/wp-admin/ HTTP/1.1" 200 12349 "http://www.example.com/wordpress/wp-login.php" "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"

LogFormat "%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i""

Symbol	        Description

%h	        IP Address of client (remote host)

%l	        Identd of client (normally unavailable)

%u	        User id of user requesting object

%t	        Time of request

%r	        Full request string

%>s	        Status code

%b	        Size of request (excluding headers)

%{Referer}i	        The previous webpage

%{User-agent}i	        The Client’s browser

# Installation 

Download Kafka and edit below two properties 

server.properties	----------> log.dirs=C:\kafka_2.11-1.0.0\kafka-logs

zookeeper.properties    ----------> dataDir=C:\kafka_2.11-1.0.0\data






