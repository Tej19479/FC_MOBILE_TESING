from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
import commos
# Desired capabilities for the Android device
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.platform_version = "10.0"
options.device_name = "DYH6QGSCSKHY598H"
options.app = "C:/Users/Tej.pratap/workscape/apk/faircentdouble/app-release (6).apk"
options.no_reset = True

# Initialize the driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Implicit wait
driver.implicitly_wait(40)
register_button = driver.find_element(By.XPATH, '//android.widget.TextView[@text="Register"]')
register_button.click()
# Frist_Middlennaem = '''//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'''
First = "//android.view.ViewGroup[2]//android.widget.EditText"
Last_Name = "//android.view.ViewGroup[3]//android.widget.EditText"
Email = "//android.view.ViewGroup[4]//android.widget.EditText"
Password = "//android.view.ViewGroup[5]//android.widget.EditText"
Mobile = "//android.view.ViewGroup[7]//android.widget.EditText"
PAN_NUMBER = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[9]/android.widget.EditText"
Aadhaar_number = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[10]/android.widget.EditText"
Date_of_birth = '''//android.widget.TextView[@text="Date of Birth "]'''
Test_data = {"First": "Tej Pratap", "Last_Name": "signh", "Email": "appium@yopmail.com", "Password": "Tej@1234",
             "Mobile": "8969490104", "PAN_NUMBER": "ISRPS996G", "Aadhaar_number": "123412341234"}

driver.find_element(By.XPATH, First).send_keys(Test_data["First"])
driver.find_element(By.XPATH, Last_Name).send_keys(Test_data["Last_Name"])
driver.find_element(By.XPATH, Email).send_keys(Test_data["Email"])
driver.find_element(By.XPATH, Password).send_keys(Test_data["Password"])
driver.find_element(By.XPATH, Mobile).send_keys(Test_data["Mobile"])
print("PAN_NUMBER")
driver.find_element(By.XPATH, PAN_NUMBER).send_keys(Test_data["PAN_NUMBER"])
driver.find_element(By.XPATH, Aadhaar_number).send_keys((Test_data["Aadhaar_number"]))
# Assuming Date_of_birth contains the XPaths for the day, month, and year fields
date_of_birth = driver.find_element(By.XPATH, Date_of_birth)
date_of_birth.click()
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "your_calendar_popup_xpath"))
# )
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "android:id/date_picker_header_date")))

# Select the year
#year_button = driver.find_element(By.ID, "android:id/date_picker_header_year")
#year_button.click()
commos.get_date_month(driver,"01 September 2006")
years_collected=commos.get_years_until_target(driver,"2000")
print(f"Collected years: {years_collected}")
