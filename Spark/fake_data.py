# Databricks notebook source
# MAGIC %md 
# MAGIC # Generate Fake Beers Drank Data
# MAGIC * [Databricks Lab Data Gen](https://github.com/databrickslabs/dbldatagen)
# MAGIC * [Faker](https://faker.readthedocs.io/en/master/)

# COMMAND ----------

# MAGIC %md ## Install Packages

# COMMAND ----------

# DBTITLE 1,Install Packages
# MAGIC %pip install dbldatagen
# MAGIC %pip install faker

# COMMAND ----------

# MAGIC %md ## Create Fake Data Available Values

# COMMAND ----------

# DBTITLE 1,Fake Values
from faker.providers.person.en import Provider

first_names = list(set(Provider.first_names))[0:1000]
brewery_beers = [
    "tinyrebel_staypuft",
    "tinyrebel_cwtch",
    "craftydevil_mikerayer",
    "craftydevil_mangowalk",
    "flowerhorn_yawn",
    "flowerhorn_mantis",
]

# COMMAND ----------

# MAGIC %md ## Create Spark DataFrame of Fake Data

# COMMAND ----------

# DBTITLE 1,Create Fake Spark DataFrame
from datetime import timedelta, datetime
from pyspark.sql.functions import current_timestamp, current_date
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    FloatType,
    TimestampType,
)
import dbldatagen as dg

interval = timedelta(days=1, hours=1)
end = datetime.now()
start = end - timedelta(30)

schema = StructType(
    [
        StructField("first_name", StringType(), True),
        StructField("brewery_beer_drank", StringType(), True),
        StructField("quantity_pint", FloatType(), True),
        StructField("timestamp", TimestampType(), True),
    ]
)

beers_drank = (
    dg.DataGenerator(sparkSession=spark, name="beers_drank", rows=10000, partitions=10)
    .withSchema(schema)
    .withColumnSpec("first_name", "string", values=first_names)
    .withColumnSpec("brewery_beer_drank", "string", values=brewery_beers)
    .withColumnSpec("quantity_pint", minValue=0.5, maxValue=1, step=0.5, random=True)
    .withColumnSpec(
        "timestamp", "timestamp", begin=start, end=end, interval=interval, random=True
    )
)

df_beers_drank = beers_drank.build(withTempView=True).withColumn(
    "last_updated", current_timestamp()
)

display(df_beers_drank.limit(10))

# COMMAND ----------

# DBTITLE 1,Also creates SQL Temp View!
# MAGIC %sql
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   beers_drank
# MAGIC LIMIT
# MAGIC   10

# COMMAND ----------

# MAGIC %md ## Create Pandas DataFrame

# COMMAND ----------

from random import randint 
from faker import Faker
import pandas as pd 
 
fake = Faker()
 
def input_data(x):
   
    # pandas dataframe
    data = pd.DataFrame()
    for i in range(0, x):
        data.loc[i,'id']= randint(1, 100)
        data.loc[i,'name']= fake.name()
        data.loc[i,'address']= fake.address()
        data.loc[i,'latitude']= str(fake.latitude())
        data.loc[i,'longitude']= str(fake.longitude())
    return data
   

input_data(10)
