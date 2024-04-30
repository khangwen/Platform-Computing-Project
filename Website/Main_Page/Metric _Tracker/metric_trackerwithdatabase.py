import time
from datetime import datetime, timedelta
from sqlite3 import Timestamp
from selenium import webdriver
import collections
import csv

#Writing to CSV file
def writeToCSV(filename: str, metrics: dict):
    with open(file = filename, mode="w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=metrics[0].keys())
        
        #Header Row
        writer.writeheader()
        
        #Data Row
        for metric in metrics:
            writer.writerow(metric)
        


def main():

    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    metrics = [] #collections.defaultdict(list)
    SAMPLE_SIZE = 3
    count = 0
    start_time = time.time()
    while count < SAMPLE_SIZE:
    # Track presence time 
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        #metrics["Presence time (Seconds)"].append(presence_time)
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled: {current_scroll}/{scroll_height} pixels")
        #metrics["Scrolling: (Pixels)"].append(current_scroll/scroll_height)

        get_title = driver.title
        print(f"Name: {get_title}")
        
        metrics.append({"TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
                        "Presence Time (Seconds)" : presence_time,
                        "Scrolling (Pixels)" : current_scroll/scroll_height,
                        "Name: ": {get_title}
                        })
        count += 1
    
        time.sleep(5) 
    
        #Get Title
        #get_title = driver.title
        #print(f"Name: {get_title}")
        #metrics["Name: "].append(get_title)

        # Track clicks   
        #python_button = driver.find_elements_by_class_name('Button1''Button2''Button3')
        #python_button.click()
        #num_clicks = 0
        
        #print(f"Number of clicks: {num_clicks}")
    
    #while True:
     #   print()
    driver.quit()
    print(metrics)
    writeToCSV("metrics.csv", metrics)
    
if __name__ == "__main__":
    main()
