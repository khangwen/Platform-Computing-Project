import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
import pandas as pd

from users import user2 as user_file2
from users import user6 as user_file6
from users import user7 as user_file7
from users import user13 as user_file13
from users import user17 as user_file17
from users import user20 as user_file20
from users import user27 as user_file27
from users import user54 as user_file54
from users import user56 as user_file56
from users import user58 as user_file58

def metricTracker(user_file, itr, group, user):
    # Set up MongoDB
    myclient = pymongo.MongoClient("mongodb+srv://khangwen197:HsUFKqdVgto1Qyo5@cluster0.pqitser.mongodb.net/")
    mydb = myclient["CSE4200"]

    mycol = mydb["Metrics4"]

    # Initialize browser
    driver = webdriver.Firefox()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

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

if __name__ == "__main__":
    metricTracker(user_file2, 0, "Control", "User2")
    metricTracker(user_file6, 0, "Control", "User6")
    metricTracker(user_file7, 0, "Control", "User7")
    metricTracker(user_file13, 0, "Control", "User13")
    metricTracker(user_file17, 0, "Control", "User17")
    metricTracker(user_file20, 0, "Control", "User20")
    metricTracker(user_file27, 0, "Control", "User27")
    metricTracker(user_file54, 0, "Control", "User54")
    metricTracker(user_file56, 0, "Control", "User56")
    metricTracker(user_file58, 0, "Control", "User58")
