import pandas as pd

cmdb_df = pd.read_csv("C:/Users/thevi/Work/PythonPandas/DataFiles/cmdb_ci_server.csv")
print(cmdb_df.shape )
print("bet we got the input finally \n")

deployedBool = cmdb_df['install_status'] == "Deployed"
pendingBool = cmdb_df['install_status'] == "Pending Deployment"
arr = [cmdb_df[deployedBool], cmdb_df[pendingBool]]
cmdb_df = pd.concat(arr)

print(cmdb_df.shape)
print("Now we only got deployed and pending deployment")

print(cmdb_df.drop_duplicates(subset=['name', 'install_status']).shape)

#done with that first filter shit