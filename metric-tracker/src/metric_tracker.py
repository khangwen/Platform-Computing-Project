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

from users import user1 as user_file1
from users import user12 as user_file12
from users import user15 as user_file15
from users import user16 as user_file16
from users import user34 as user_file34
from users import user35 as user_file35
from users import user40 as user_file40
from users import user42 as user_file42
from users import user47 as user_file47
from users import user60 as user_file60

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
    group1 = "Control"  
    group2 = "Test"

    metricTracker(user_file2, 0, group1, "User2")
    metricTracker(user_file6, 0, group1, "User6")
    metricTracker(user_file7, 0, group1, "User7")
    metricTracker(user_file13, 0, group1, "User13")
    metricTracker(user_file17, 0, group1, "User17")
    metricTracker(user_file20, 0, group1, "User20")
    metricTracker(user_file27, 0, group1, "User27")
    metricTracker(user_file54, 0, group1, "User54")
    metricTracker(user_file56, 0, group1, "User56")
    metricTracker(user_file58, 0, group1, "User58")

    metricTracker(user_file1, 0, group2, "User1")
    metricTracker(user_file12, 0, group2, "User12")
    metricTracker(user_file15, 0, group2, "User15")
    metricTracker(user_file16, 0, group2, "User16")
    metricTracker(user_file34, 0, group2, "User34")
    metricTracker(user_file35, 0, group2, "User35")
    metricTracker(user_file40, 0, group2, "User40")
    metricTracker(user_file42, 0, group2, "User42")
    metricTracker(user_file47, 0, group2, "User47")
    metricTracker(user_file60, 0, group2, "User60")
