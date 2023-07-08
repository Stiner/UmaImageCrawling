from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

char_image_list = []

uma_list_url = "https://umamusume.jp/character"
download_dir = "./downloads/"

options = webdriver.EdgeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
driver = webdriver.Edge(options=options)

driver.get(url=uma_list_url)

last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

total_count = len(driver.find_element(By.CLASS_NAME, "character__list").find_elements(By.CLASS_NAME, "anime-show"))

print("Total:" + str(total_count))

for i in range(0, total_count):
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    xpath_a = "/html/body/div[1]/div/div/div[2]/section/div/section[1]/ul/li[" + str(i + 1) + "]/a"
    element_a = driver.find_element(By.XPATH, xpath_a)

    element_attr = str(element_a.get_attribute("href"))
    char_name_en = element_attr.replace("https://umamusume.jp/character/detail/?name=", "");

    element_a.click()
    time.sleep(2)

    xpath_char = "/html/body/div[1]/div/div/div[2]/section/div/div/section[1]/div[1]"
    element_char_detail = driver.find_element(By.XPATH, xpath_char)

    image_count = len(element_char_detail.find_elements(By.TAG_NAME, "img"))
    print("Image:" + str(image_count))

    for j in range(0, image_count):
        xpath_img = "/html/body/div[1]/div/div/div[2]/section/div/div/section[1]/div[1]/img[" + str(j + 1) + "]"
        element_img = driver.find_element(By.XPATH, xpath_img)

        char_name_jp = str(element_img.get_attribute("alt")).replace("<small>", "").replace("</small>", "").replace("<br>", " ")
        image_url = str(element_img.get_attribute("src"))

        print("{:02}/{:02}-{:02}/{:02}|{}|{}|{}".format(i + 1, total_count, j + 1, image_count, char_name_en, char_name_jp, image_url))

        char_image_list.append({ char_name_en, char_name_jp, image_url })

        file_ext = os.path.splitext(image_url)[1]
        file_name = "{:02}-{:02}_{}_{}{}".format(i + 1, j + 1, char_name_en, char_name_jp, file_ext)
        urlretrieve(image_url, os.path.join(download_dir, file_name))

    driver.back()
    time.sleep(2)

driver.close()
