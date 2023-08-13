# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "255c87ad-76bb-4712-9fdf-fefe03baf6d5",
"fs.azure.account.oauth2.client.secret": 'd1B8Q~6f86eiDHhzdH~hkVUDao0BGBuXm66VScs5',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/65ec0a32-2c09-4d55-8134-b0938bc3aaac/oauth2/token"}


dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicdata123.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolympic",
extra_configs = configs)

# COMMAND ----------


