# spark_testing
Code for setting up and testing Apache Spark

Installation instructions:

$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install python-software-properties -y

$ sudo apt-add-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java7-installer -y

$ sudo apt-get install scala -y
$ scala # make sure scala works

$ mkdir spark
$ cd spark
$ wget http://d3kbcqa49mib13.cloudfront.net/spark-1.3.1.tgz
$ gunzip -c spark-1.3.1.tgz | tar -xvf -
$ cd spark-1.3.1/
$ sudo build/sbt assembly

add /usr/local/spark/bin to PATH in .bashrc:
export PATH=/usr/local/spark/bin:$PATH

test:
$ run-example SparkPi 10

run python REPL:
$ pyspark
