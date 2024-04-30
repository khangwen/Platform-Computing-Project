from itertools import count
from os import link
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Using true or false instead of bool to see if keywords exists
def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        #print(driver.page_source.lower())
        return True
    else:
        return False

#Returns number of iamges on a webpage
def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

#Tracking the users clicks on links
#def clickLink(driver, tag_name)->bool:
 #   click = 0
  #  for link in tag_name:
   #     click += len(driver.find_elements(By.TAG_NAME, link))
    #    return click
   # for link in links:
    #        link.click()
    
    

#Combining Keywords, Link, Image Affinities
def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORDS":
        for keywords in req_list: 
            if findText(driver, keywords):
                print("Keywords Found:", keywords)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("Sorry, these keywords were not found:", keywords)
                
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time*num_images
        time.sleep(total_reward_time)
        
   # elif action.upper() == "LINK":
     #     for link in req_list:
      #        if clickLink(driver, link):
       #           total_reward_time = reward_time*link
        #          time.sleep(reward_time)
                 
            
            
    return total_reward_time


def main():

    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reward_time = 10
    
    total_reward_time  = userAction("KEYWORDS", driver, reward_time, ["DNA", "you", "eggs", "milk"])
    tag_name = ["img"]
    total_reward_time += userAction("IMAGE", driver, reward_time, tag_name)
    
    #link = ["a"]
    #total_reward_time += userAction("LINK", driver, reward_time, link)
    
    
    driver.quit()
    print("Presence Time:", total_reward_time, "seconds")
    
if __name__ == "__main__":
    main()