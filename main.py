from __future__ import print_function
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("datasource-postgres").config("spark.jars", "postgresql-42.3.1.jar").getOrCreate()

# Create a PySpark DataFrame from an RDD consisting of a list of tuples.
dataList = sparkSession.sparkContext.parallelize([(1, "Ali", 19), (2, "Tom", 20)])
schema = StructType([StructField("id", IntegerType(), False),
                     StructField("name", StringType(), False),
                     StructField("age", IntegerType(), False)])
dataFrame = sparkSession.createDataFrame(dataList, schema)
dataFrame.show()

# connect to DB to write
format = "jdbc"
truncate = "true"
driver = "org.postgresql.Driver"
_url = "jdbc:postgresql://localhost:5432/test"
dbtable = "my_sample_table"
user = "test"
password = "test"
mode = "overwrite"

dataFrame.write.format(format).option("driver", driver).option("url", _url).option("user", user).option("password", password).option("dbtable", dbtable).mode(mode).save()

# connect to DB to read
readDataFrame = sparkSession.read.format(format).option("driver", driver).option("url", _url).option("user", user).option("password", password).option("dbtable", dbtable).load()
readDataFrame.show()
readDataFrame.printSchema()




