import json
import os
import re
import time

from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Load .env file
load_dotenv()

# Set FB account and password
fb_account = os.getenv('FB_ACCOUNT')
fb_password = os.getenv('FB_PASSWORD')

# Use webdriver_manager to automatically download and manage ChromeDriver
options = Options()
options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open Facebook login page
driver.get("https://www.facebook.com/")

# Enter Facebook login information
email = fb_account
password = fb_password

# Find input field and enter email
driver.find_element(By.ID, "email").send_keys(email)

# Find input field and enter password
driver.find_element(By.ID, "pass").send_keys(password)

# Click the login button
driver.find_element(By.NAME, "login").click()

# Wait a few seconds to ensure successful login
time.sleep(20)

# Read group links from input.txt
with open("input.txt", "r") as file:
    group_links = file.readlines()

for index, group_link in enumerate(group_links, start=1):
    group_url = group_link.strip() + "/?sorting_setting=CHRONOLOGICAL"
    driver.get(group_url)

    # Double click in the top left corner of the browser to ignore pop-ups and ensure the click position is within the window
    ActionChains(driver).move_by_offset(0, 0).click().click().perform()

    # Wait a few seconds to ensure the page loads completely
    time.sleep(5)

    # Initialize variables to control the crawl stop condition
    continue_scrolling = True
    posts_data = []

    while continue_scrolling:

        # Scrape posts from the current page
        posts = driver.find_elements(By.CSS_SELECTOR, "div[class*='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
        for post in posts:
            try:
                # Scrape post timestamp
                timestamp = post.find_element(By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs a").text
                if re.search(r"\d+天|\d+月\d+日[上下]午\d+:\d+", timestamp):
                    print("Post timestamp exceeds one day, crawler terminated.")
                    continue_scrolling = False
                    break
                
                # Check if there is a 'See More' button, if yes, click to expand content
                see_more_button = post.find_elements(By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1sur9pj.xkrqix3.xzsf02u.x1s688f[role='button'][tabindex='0']")
                if see_more_button:
                    see_more_button[0].click()
                    time.sleep(0.5)
                
                # Scrape post author
                author = post.find_element(By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs").text

                # Scrape post content
                content_elements = post.find_elements(By.CSS_SELECTOR, "div.xu06os2.x1ok221b")
                if len(content_elements) >= 3:
                    content = content_elements[2].get_attribute('innerText')
                else:
                    content = ""

                # Ensure author, timestamp, and content have values
                if author and timestamp and content:
                    # Use a composite unique key to check if the post already exists
                    post_key = f"{author}-{timestamp}"
                    if post_key not in [f"{p['發文者:']}-{p['發文時間:']}" for p in posts_data]:
                        post_data = {
                            "發文者:": author,
                            "發文時間:": timestamp,
                            "內文:": content
                        }
                        posts_data.append(post_data)
                        print("發文者:", author)
                        print("發文時間:", timestamp)
                        print("內文:", content)
                        print("-----------------------------------")
                    else:
                        continue # Duplicate post, continue scrolling
                else:
                    continue # Incomplete post data, continue scrolling
            
            except:
                continue # Unable to scrape related elements, continue scrolling

            # Scroll 1/10 of the page to load more posts
        driver.execute_script("window.scrollBy(0, window.innerHeight / 10);")
        time.sleep(0.5)  # Wait for the page to load new posts

    # Write the information to a file
    today_date = datetime.now().strftime("%Y%m%d")
    output_filename = f"{today_date}_{index}.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(posts_data, f, ensure_ascii=False, indent=4)

# Close the browser
driver.quit()
