import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
import pandas as pd

from users import user1 as user_file

# Set up MongoDB
myclient = pymongo.MongoClient("mongodb+srv://khangwen197:HsUFKqdVgto1Qyo5@cluster0.pqitser.mongodb.net/")
mydb = myclient["CSE4200"]

mycol = mydb["Metrics3"]

# Initialize browser
driver = webdriver.Firefox()

# Navigate to your website 
driver.get("http://localhost:3000/")

# Metric info
itr = 0
group = "Control"
user = "user1"

# Track presence time 
start_time = time.time()
presence_time = start_time

# User action
user_file.userAction(driver)

# Calculate presence time
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")
    
# Insert data into MongoDB
new_entry = {"Iteration": itr, "Group": group, "User": user, "PRESENCE_TIME (SEC.)": presence_time}
mycol.insert_one(new_entry)
        
# Close browser
driver.quit()

# Print data from MongoDB as table
print("\nData from MongoDB:")
metric_data = [data for data in mycol.find()]
df_metric_data = pd.DataFrame(metric_data)
print(df_metric_data.sort_values(by=["Group", "User"]))