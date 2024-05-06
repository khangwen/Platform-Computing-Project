import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo

from users.user3 import userAction

# Set up MongoDB
myclient = pymongo.MongoClient("mongodb+srv://khangwen197:HsUFKqdVgto1Qyo5@cluster0.pqitser.mongodb.net/")
mydb = myclient["CSE4200"]

mycol = mydb["Metrics2"]

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
userAction(driver)

# Calculate presence time
current_time = time.time()
presence_time = current_time - start_time
print(f"Presence time: {presence_time} seconds")
    
# Insert data into MongoDB
new_entry = {"Iteration": itr, "Group": group, "User": user, "PRESENCE_TIME (SEC.)": presence_time}
mycol.insert_one(new_entry)
        
driver.quit()