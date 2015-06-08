# start shell using
#SPARK_CLASSPATH=/home/phil/D/Users/philipp.deutsch/postgresql-9.4-1201.jdbc4.jar pyspark

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)

#load table into dataframe
df = (sqlContext
        .load(source="jdbc",
              url="jdbc:postgresql://[HOSTNAME]/[DBNAME]?user=[USERNAME]&password=[PASSWORD]",
              dbtable="[TABLE]")
     )

#print first row of dataframe
print(df.take(1))
