-- Databricks notebook source
-- MAGIC %md
-- MAGIC ##### Drop all the tables
-- MAGIC - This notebook drops the pocessed and the presentation DB
-- MAGIC - In the data pipeline raw is extenal and other 2 are managed tables.
-- MAGIC - Following this run the Ingest All Data file. 

-- COMMAND ----------

DROP DATABASE IF EXISTS f1_processed CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS f1_processed
LOCATION "/mnt/adcd4hpstorage/processed";

-- COMMAND ----------

DROP DATABASE IF EXISTS f1_presentation CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS f1_presentation 
LOCATION "/mnt/adcd4hpstorage/presentation";

-- COMMAND ----------


