# Databricks notebook source
# MAGIC %md
# MAGIC # Spark Cheatsheet!

# COMMAND ----------

# MAGIC %md ## Did you know...?

# COMMAND ----------

# DBTITLE 1,What version of spark am I using..
sc.version

# COMMAND ----------

# DBTITLE 1,The help command is your friend for any python objects...
help(sc)  ## spark context

# COMMAND ----------

# DBTITLE 1,The help command is your friend for the filesystem commands....
# MAGIC %fs help

# COMMAND ----------

# DBTITLE 1,Databricks has datasets...
display(dbutils.fs.ls("/databricks-datasets"))

# COMMAND ----------

# DBTITLE 1,You can embed HTML...
html = """<h1>Wowzers</h1><p>This html could be anything you wanted... Anything! Say a picture of a dog...</p><img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Staffie.jpg/640px-Staffie.jpg'</img>"""
displayHTML(html)

# COMMAND ----------

# DBTITLE 1,You can set and use global variables for SQL Commands...
spark.conf.set(
    "dgrf.flights.path", "dbfs:/databricks-datasets/flights/departuredelays.csv"
)

# COMMAND ----------

# DBTITLE 1,See...
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS flights;
# MAGIC CREATE TABLE IF NOT EXISTS flights USING CSV OPTIONS (header = true, path = "${dgrf.flights.path}");
# MAGIC --using variable
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   flights;

# COMMAND ----------

# MAGIC %md ## Create Basic Dataframe
# MAGIC * [Databricks Data Generator](https://github.com/databrickslabs/dbldatagen)
# MAGIC
# MAGIC The following will create a dataframe called **df_beers_drank**, a temporary SQL view called **beers_drank**, a pandas dataframe called **pdf_beers_drank** and a reference data frame called **df_brewers**. This is all generated from the [fake_data notebook]($./fake_data).

# COMMAND ----------

# DBTITLE 1,Create Fake Data Objects
# MAGIC %run ./fake_data

# COMMAND ----------

# MAGIC %md ## Import all Our Dependencies
# MAGIC * **Make sure you do this so that all the other commands in this notebook work!**

# COMMAND ----------

from pyspark.sql.functions import (
    col,
    current_timestamp,
    collect_list,
    collect_set,
    explode,
    split,
    sum,
    min,
    desc,
    cast,
    date_format,
    date_add,
    year,
    dayofweek,
)
from datetime import datetime, timedelta

# COMMAND ----------

# MAGIC %md ## Basic Queries

# COMMAND ----------

# DBTITLE 1,Print Schema
df_beers_drank.printSchema()

# COMMAND ----------

# DBTITLE 1,Show Data
df_beers_drank.show(n=5, truncate=False)

# COMMAND ----------

# DBTITLE 1,Display Data
display(df_beers_drank)

# COMMAND ----------

# DBTITLE 1,Summary Stats
df_beers_drank.summary().show()

# COMMAND ----------

# DBTITLE 1,Query SQL Via SQL Method in Python
display(spark.sql("SELECT * FROM beers_drank LIMIT 10"))

# COMMAND ----------

# DBTITLE 1,Query Using SQL Magic Command with Group By
# MAGIC %sql
# MAGIC SELECT
# MAGIC   brewery_beer,
# MAGIC   sum(quantity_pint) AS pints_drank
# MAGIC FROM
# MAGIC   beers_drank
# MAGIC GROUP BY
# MAGIC   brewery_beer

# COMMAND ----------

# DBTITLE 1,Select DataFrame Columns in all Sorts of Ways and Filter
df_select = df_beers_drank.select(
    col("first_name"), df_beers_drank.brewery_beer, "timestamp"
).filter(col("quantity_pint") == 1)
display(df_select)

# COMMAND ----------

# DBTITLE 1,Explain a Query Plan
df_select.explain()

# COMMAND ----------

# DBTITLE 1,Beers Drank Aggregated Grouped by Brewer with Or Filter
df_group = (
    df_beers_drank.groupBy(col("brewery_beer"))
    .agg(
        sum(col("quantity_pint")).alias("pints_drank"),
        min(col("timestamp")).alias("earliest_date"),
    )
    .filter(
        (
            col("brewery_beer").contains("crafty")
            | col("brewery_beer").contains("flower")
        )
    )
)
display(df_group)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates and Order Asc with Distinct and orderBy
df_sort1 = (
    df_beers_drank.select(col("first_name")).distinct().orderBy(col("first_name").asc())
)
display(df_sort1)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates and Order Desc with dropDuplicates on Specific Columns and Sort
df_sort2 = (
    df_beers_drank.select("brewery_beer", "first_name", "quantity_pint")
    .dropDuplicates(["brewery_beer", "quantity_pint"])
    .sort(desc("brewery_beer"))
)
display(df_sort2)

# COMMAND ----------

# DBTITLE 1,Drop Columns and Add A Constant as Column
df_constant = df_beers_drank.drop("last_updated").withColumn("tax", lit(17.5))
display(df_constant)

# COMMAND ----------

# MAGIC %md ## Write & Read

# COMMAND ----------

# DBTITLE 1,Set Scratch Path Variable in DBFS
scratch_file_path = "dbfs:/myscratchpad/"

# COMMAND ----------

# DBTITLE 1,Write to CSV
df_beers_drank.write.mode("overwrite").option("header", "true").csv(
    scratch_file_path + "/csv"
)

# COMMAND ----------

# DBTITLE 1,Red from CSV with Show
spark.read.option("header", "true").option("inferSchema", "true").option(
    "delimiter", ","
).csv(scratch_file_path + "/csv").show()

# COMMAND ----------

# DBTITLE 1,Write to Delta
df_beers_drank.write.format("delta").mode("overwrite").save(
    scratch_file_path + "/delta"
)

# COMMAND ----------

# DBTITLE 1,Read from Delta with Show No Truncate Five Rows
spark.read.format("delta").load(scratch_file_path + "/delta").show(truncate=False, n=5)

# COMMAND ----------

# DBTITLE 1,Clean Up!
dbutils.fs.rm(scratch_file_path, True)

try:
    dbutils.fs.ls(scratch_file_path)
except:
    print("Good: Data Cleared!")
else:
    raise ("Bad: Data Remains!")

# COMMAND ----------

# MAGIC %md ## Funky Commands

# COMMAND ----------

# DBTITLE 1,Collect to Get all Rows and Pick First One from List of Rows
first_brewer_beer_row = (
    df_beers_drank.select(col("brewery_beer")).distinct().collect()[0]
)
print(f"The first row is {first_brewer_beer_row}")
first_brewer_beer = first_brewer_beer_row[0]
print(f"The first value in the first row is {first_brewer_beer}")

# COMMAND ----------

# DBTITLE 1,Get All Beers Drank by Each Name Using Collect List (not distinct)
df_beers_collected = (
    df_beers_drank.groupBy("first_name")
    .agg(collect_list("brewery_beer").alias("brewery_beers_drank"))
    .orderBy("first_name")
)
display(df_beers_collected)

# COMMAND ----------

# DBTITLE 1,Explode the Collected List Back!
df_beers_exploded = df_beers_collected.select(
    "first_name", explode("brewery_beers_drank")
).orderBy("first_name")
display(df_beers_exploded)

# COMMAND ----------

# DBTITLE 1,Get All Beers Drank by Each Name Using Collect Set (distinct)
df_beers_collected = (
    df_beers_drank.groupBy("first_name")
    .agg(collect_set("brewery_beer").alias("unique_beers_drank"))
    .orderBy("first_name")
)
display(df_beers_collected)

# COMMAND ----------

# DBTITLE 1,Split Brewers & Beers with Drop Columns & Filtered with StartsWith
df_beers_split = (
    df_beers_drank.withColumn("brewer", split(col("brewery_beer"), "_")[0])
    .withColumn("beer", split(col("brewery_beer"), "_")[1])
    .filter(col("brewery_beer").startswith("tinyrebel"))
    .drop("timestamp", "last_updated", "brewery_beer")
)
display(df_beers_split)

# COMMAND ----------

# MAGIC %md ## Date and Time

# COMMAND ----------

# DBTITLE 1,Simple date and time functions
df_dates = (
    df_beers_drank.withColumn("date_cast", col("timestamp").cast("date"))
    .withColumn("date_format", date_format(col("timestamp"), "dd-MMM-yyyy"))
    .withColumn("date_add", date_add(col("timestamp"), 1))
    .withColumn("year", year(col("timestamp")))
    .withColumn("dayofweek", dayofweek(col("timestamp")))
).select("timestamp", "date_cast", "date_format", "date_add", "year", "dayofweek")
display(df_dates)

# COMMAND ----------

# MAGIC %md ## Create Functions

# COMMAND ----------

# DBTITLE 1,Create Simple Function
import random


def random_beer_reaction():
    reaction = ["bleh!", "tasty!", "woshiss??"]
    i = random.randint(0, 2)
    return reaction[i]


random_beer_reaction()

# COMMAND ----------

# DBTITLE 1,Create Simple Function with Type Hints
# Our input/output is a string
@udf("string")
def random_beer_reaction_tudf(beer: str) -> str:
    reaction = ["bleh!", "tasty!", "woshiss??"]
    i = random.randint(0, 2)
    return reaction[i]

# COMMAND ----------

# DBTITLE 1,Pandas Vectorised Function
import pandas as pd
from pyspark.sql.functions import pandas_udf

# We have a integer input/output
@pandas_udf("integer")
def get_beer_cost_vudf(quantity_pint: pd.Series) -> pd.Series:
    return quantity_pint * 4.0

# COMMAND ----------

# DBTITLE 1,Register for use in Python and SQL
random_beer_reaction_udf = udf(random_beer_reaction)
spark.udf.register("random_beer_reaction_udf", random_beer_reaction)
spark.udf.register("random_beer_reaction_tudf", random_beer_reaction_tudf)
spark.udf.register("get_beer_cost_vudf", get_beer_cost_vudf)

# COMMAND ----------

# DBTITLE 1,Functions in Python
df_reaction = (
    df_beers_drank.withColumn("beer_reaction_udf", random_beer_reaction_udf())
    .withColumn("beer_reaction_tudf", random_beer_reaction_tudf(col("brewery_beer")))
    .withColumn("beer_cost_vudf", get_beer_cost_vudf(col("quantity_pint")))
    .select("brewery_beer", "beer_reaction_udf", "beer_reaction_tudf", "beer_cost_vudf")
)
display(df_reaction)

# COMMAND ----------

# DBTITLE 1,Registered Functions in SQL
# MAGIC %sql
# MAGIC -- You can now also apply the UDF from SQL
# MAGIC SELECT
# MAGIC   brewery_beer,
# MAGIC   random_beer_reaction_udf() AS random_beer_reaction,
# MAGIC   get_beer_cost_vudf(quantity_pint) as beer_cost
# MAGIC FROM
# MAGIC   beers_drank

# COMMAND ----------

# MAGIC %md ## RePartioning

# COMMAND ----------

# DBTITLE 1,Get Partitions of DataFrame
df_beers_drank.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 1,Reduce Partitions Using Coalesce without Shuffle
df_beers_drank_coalesce = df_beers_drank.coalesce(2)
df_beers_drank_coalesce.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 1,Reduce or Increase Partitions Using Repartition Always with Shuffle
df_beers_drank_repartition = df_beers_drank.repartition(8)
df_beers_drank_repartition.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md ## Caching

# COMMAND ----------

# DBTITLE 1,Cache DataFrame and Perform Action to Cache
df_beers_drank.cache()
df_beers_drank.count()

# COMMAND ----------

# DBTITLE 1,Remove from Cache
df_beers_drank.unpersist()
