# Databricks notebook source
# MAGIC %md
# MAGIC Esto es una prueba de workflow con ejecucion de llamada a un API

# COMMAND ----------

# MAGIC %sh echo "Hello, I´m sending Metrics for Monitoring Service"

# COMMAND ----------

# MAGIC %sh sudo apt install curl

# COMMAND ----------

# MAGIC %sh curl https://www.google.com/accounts/ClientLogin \
# MAGIC --data-urlencode Email=brad.gushue@example.com --data-urlencode Passwd=new+foundland \
# MAGIC -d accountType=GOOGLE \
# MAGIC -d source=Google-cURL-Example \
# MAGIC -d service=lh2

# COMMAND ----------

# MAGIC %sh echo "Finished the Metrics for Monitoring Service"

# COMMAND ----------


