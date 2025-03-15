# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount Azure Data Lake using Service Principal

# COMMAND ----------

# MAGIC %md
# MAGIC ### Functions to mount container from ADLS
# MAGIC - The following Secrets has been stored in Azure Key Vault

# COMMAND ----------

def mount_adls(storage_account_name, container_name):
    # Get secrets from Key Vault
    client_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'client-id')
    tenant_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'tenant-id')
    client_secret = dbutils.secrets.get(scope = 'formula1-scope', key = 'client-secret')
    
    # Set spark configurations
    configs = {"fs.azure.account.auth.type": "OAuth",
              "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
              "fs.azure.account.oauth2.client.id": client_id,
              "fs.azure.account.oauth2.client.secret": client_secret,
              "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    
    # Unmount the mount point if it already exists
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}")
    
    # Mount the storage account container
    dbutils.fs.mount(
      source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
      mount_point = f"/mnt/{storage_account_name}/{container_name}",
      extra_configs = configs)
    
    display(dbutils.fs.mounts())

# COMMAND ----------

mount_adls('adcd4hpstorage', 'raw')

# COMMAND ----------

mount_adls("adcd4hpstorage","processed")

# COMMAND ----------

mount_adls("adcd4hpstorage","presentation")

# COMMAND ----------

mount_adls("adcd4hpstorage","demo")

# COMMAND ----------

# MAGIC %md
# MAGIC - We’ll use Medieelion Architecture with three layers: Raw, Processed, and Presentation.
# MAGIC - Raw layer will handle data input, Processed will transform it, and Presentation will manage the UI.
# MAGIC - This setup ensures clean structure and easy maintenance.
