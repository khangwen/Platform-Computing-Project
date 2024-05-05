import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website
website_URL = "http://localhost:3000/"
driver.get(website_URL)

# Wait for the page to fully load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Track presence time
start_time = time.time()
presence_time = start_time

# Function to count elements by tag name
def countElem(driver, tag_name):
    return len(driver.find_elements(By.TAG_NAME, tag_name))

# Function to download images
def download_images(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    image_PATH = 'scraped_images/'
    if not os.path.exists(image_PATH):
        os.makedirs(image_PATH)
    counter = 0
    for image in images:
        counter += 1
        new_url = image_PATH + "test" + str(counter) + ".png"
        src = image.get_attribute("src")
        urllib.request.urlretrieve(src, new_url)

# Function to count instances of a keyword in the page source
def count_instances(page_source, keyword):
    return page_source.lower().count(keyword.lower())

# Function to count images in the page source
def count_images(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return len(soup.find_all('img'))

# Function to count URLs in the page source
def count_urls(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return len(soup.find_all('a', href=True))

# Main script execution
try:
    # Count and interact with buttons
    tags = ["button"]
    total_reward_time = 0
    for tag in tags:
        num_buttons = countElem(driver, tag)
        total_reward_time += 10 * num_buttons
        time.sleep(10)

    # Download images
    download_images(driver)

    # Count instances of a keyword, images, and URLs in the webpage content
    page_source = driver.page_source
    keyword_count = count_instances(page_source, "school")
    images_count = count_images(page_source)
    urls_count = count_urls(page_source)

    # Print individual counts
    print("Keyword Instances:", keyword_count)
    print("Image Instances:", images_count)
    print("URL Instances:", urls_count)

    # Output presence time
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")

except TimeoutException:
    print("Page load timed out")
finally:
    # Close the webdriver
    driver.quit()
