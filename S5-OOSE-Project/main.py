# A S Nandanunni
# 20219023
# CS A

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


try:
    # Navigate to page
    driver.get("https://www.weathercity.com/")
    countries = driver.find_elements(By.TAG_NAME, "a")
    for country in countries:
        if country.text == "India":
            driver.get(country.get_attribute("href"))
            cities = driver.find_elements(By.TAG_NAME, "a")
            for city in cities:
                if city.text == "Ernakulam":
                    driver.get(city.get_attribute("href"))
                    time.sleep(10)
except Exception as err:
    print(str(err))
finally:
    driver.quit()
