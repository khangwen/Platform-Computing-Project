import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def countElem(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():

    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time  = 0
    tags = ["header"] 
    for tag in tags:
        num_header = countElem(driver, tag)
        total_reward_time += reward_time*num_header
        time.sleep(reward_time)
      
    print("Presence Time:", total_reward_time, "seconds")
   
    print("There are:", num_header, "titles")
    
    driver.quit()
    
if __name__ == "__main__":
    main()