import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
import pandas as pd

# Import users for iterative testing
# Group 1 users ~ 24 total
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

from users import user3 as user_file3
from users import user8 as user_file8
from users import user22 as user_file22
from users import user23 as user_file23
from users import user25 as user_file25
from users import user30 as user_file30
from users import user32 as user_file32
from users import user33 as user_file33
from users import user41 as user_file41
from users import user43 as user_file43
from users import user46 as user_file46
from users import user48 as user_file48
from users import user51 as user_file51
from users import user57 as user_file57

# Group 2 users ~ 25 total
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

from users import user5 as user_file5
from users import user10 as user_file10
from users import user14 as user_file14
from users import user21 as user_file21
from users import user24 as user_file24
from users import user26 as user_file26
from users import user31 as user_file31
from users import user39 as user_file39
from users import user44 as user_file44
from users import user45 as user_file45
from users import user52 as user_file52
from users import user53 as user_file53
from users import user55 as user_file55
from users import user59 as user_file59
from users import user61 as user_file61

def metricTracker(user_file, itr, group, user):
    # Set up MongoDB
    myclient = pymongo.MongoClient("mongodb+srv://khangwen197:HsUFKqdVgto1Qyo5@cluster0.pqitser.mongodb.net/")
    mydb = myclient["CSE4200"]

    mycol = mydb["Iteration4_Metrics"]

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
    group1 = "Final"  
    group2 = "Final"
    group3 = "Final"
    iteration = 4

    #metricTracker(user_file2, iteration, group1, "User2")
    #metricTracker(user_file6, iteration, group1, "User6")
    metricTracker(user_file7, iteration, group1, "User7")
    metricTracker(user_file13, iteration, group1, "User13")
    metricTracker(user_file17, iteration, group1, "User17")
    metricTracker(user_file20, iteration, group1, "User20")
    metricTracker(user_file27, iteration, group1, "User27")
    metricTracker(user_file54, iteration, group1, "User54")
    metricTracker(user_file56, iteration, group1, "User56")
    metricTracker(user_file58, iteration, group1, "User58")

    # metricTracker(user_file3, iteration, group1, "User3")
    # metricTracker(user_file8, iteration, group1, "User8")
    # metricTracker(user_file22, iteration, group1, "User22")
    # metricTracker(user_file23, iteration, group1, "User23")
    # metricTracker(user_file25, iteration, group1, "User25")
    # metricTracker(user_file30, iteration, group1, "User30")
    # metricTracker(user_file32, iteration, group1, "User32")
    # metricTracker(user_file33, iteration, group1, "User33")
    # metricTracker(user_file41, iteration, group1, "User41")
    # metricTracker(user_file43, iteration, group1, "User43")
    # metricTracker(user_file46, iteration, group1, "User46")
    # metricTracker(user_file48, iteration, group1, "User48")
    # metricTracker(user_file51, iteration, group1, "User51")
    # metricTracker(user_file57, iteration, group1, "User57")

    # metricTracker(user_file1, iteration, group2, "User1")
    # metricTracker(user_file12, iteration, group2, "User12")
    # metricTracker(user_file15, iteration, group2, "User15")
    # metricTracker(user_file16, iteration, group2, "User16")
    # metricTracker(user_file34, iteration, group2, "User34")
    # metricTracker(user_file35, iteration, group2, "User35")
    # metricTracker(user_file40, iteration, group2, "User40")
    # metricTracker(user_file42, iteration, group2, "User42")
    # metricTracker(user_file47, iteration, group2, "User47")
    # metricTracker(user_file60, iteration, group2, "User60")

    # metricTracker(user_file5, iteration, group2, "User5")
    # metricTracker(user_file10, iteration, group2, "User10")
    # metricTracker(user_file14, iteration, group2, "User14")
    # metricTracker(user_file21, iteration, group2, "User21")
    # metricTracker(user_file24, iteration, group2, "User24")
    # metricTracker(user_file26, iteration, group2, "User26")
    # metricTracker(user_file31, iteration, group2, "User31")
    # metricTracker(user_file39, iteration, group2, "User39")
    # metricTracker(user_file44, iteration, group2, "User44")
    # metricTracker(user_file45, iteration, group2, "User45")
    # metricTracker(user_file52, iteration, group2, "User52")
    # metricTracker(user_file53, iteration, group2, "User53")
    # metricTracker(user_file55, iteration, group2, "User55")
    # metricTracker(user_file59, iteration, group2, "User59")
    # metricTracker(user_file61, iteration, group2, "User61")

