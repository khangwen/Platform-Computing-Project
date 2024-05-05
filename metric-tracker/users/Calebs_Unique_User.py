from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time

def count_instances(page_source, keyword):
    return page_source.lower().count(keyword.lower())

def count_images(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return len(soup.find_all('img'))

def count_urls(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return len(soup.find_all('a', href=True))

def main(file_path, keyword):
    start_time = time.time()  # Record the start time

    # Set up Selenium webdriver
    driver = webdriver.Chrome()

    try:
        # Open the local HTML file
        driver.get("file://" + os.path.abspath(file_path))

        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Get the HTML source of the webpage
        page_source = driver.page_source

        # Count instances of keyword, images, and URLs in the webpage content
        keyword_count = count_instances(page_source, keyword)
        images_count = count_images(page_source)
        urls_count = count_urls(page_source)

        # Print individual counts
        print("Keyword Instances:", keyword_count)
        print("Image Instances:", images_count)
        print("URL Instances:", urls_count)

        # Sum up the total number of instances for all elements
        total_instances = keyword_count + images_count + urls_count

        return total_instances

    except TimeoutException:
        print("Page load timed out")
    finally:
        end_time = time.time()  # Record the end time
        duration = end_time - start_time  # Calculate the duration
        print("Duration:", duration, "seconds")

        # Close the webdriver
        driver.quit()

if __name__ == "__main__":
    file_path = r"C:\Users\caleb\OneDrive\Documents\cse4500\assignment_1\aboutME.html"
    keyword = "school"  # Keyword to search for

    print("Running script against the local HTML file:")
    total_instances = main(file_path, keyword)
    if total_instances is not None:
        print("Total Instances:", total_instances)
