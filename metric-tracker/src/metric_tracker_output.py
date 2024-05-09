import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
import pandas as pd

# Set up MongoDB
myclient = pymongo.MongoClient("mongodb+srv://khangwen197:HsUFKqdVgto1Qyo5@cluster0.pqitser.mongodb.net/")
mydb = myclient["CSE4200"]

mycol = mydb["Metrics3"]

# Print data from MongoDB as table
print("\nData from MongoDB:")
metric_data = [data for data in mycol.find()]
df_metric_data = pd.DataFrame(metric_data)
# df_metric_data.to_csv('out.csv', index=False)  
print(df_metric_data.sort_values(by=["Group", "User"]))