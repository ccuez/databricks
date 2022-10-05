# Databricks notebook source
# MAGIC %md
# MAGIC Esto es una prueba de workflow task2

# COMMAND ----------

def get_argument_value_or_default(name, default):
  value = getArgument(name)
  if len(value) < 1:
    return default
  return value


def str_to_bool(value):
  FALSE_VALUES = ['False', 'false', 'no', '0']
  TRUE_VALUES = ['True', 'true', 'yes', '1']
  lvalue = str(value).lower()
  if lvalue in (FALSE_VALUES): return False
  if lvalue in (TRUE_VALUES):  return True
  raise Exception("String value should be one of {}, but got '{}'.".format(FALSE_VALUES + TRUE_VALUES, value))
    

# COMMAND ----------

job_fail = str_to_bool(get_argument_value_or_default("job_fail", False))

print ( "job_fail value is: " + str(job_fail))

# COMMAND ----------

import time
print( "Hello, I´m training the model")
print( "Sleeping 30 sec")
time.sleep(30)

# COMMAND ----------

# Se sale sin ejecutar el resto del codigo que haya por detras pero sin error
#  return dbutils.notebook.exit(" job_fail value is: '{}' ".format(job_fail))
# Si queremos salir con error es lanzando una excepcion
  
if job_fail:
  raise Exception("Training failed")
else:
  print( "Training Sucessfully")
