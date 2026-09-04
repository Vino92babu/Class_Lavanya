from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

'''
#Drop_down_Static 
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
driver.find_element(By.ID,"password").send_keys("Learning@830$3mK2")
Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_value("teach")
Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_index(0)
Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_visible_text("Consultant")

'''

'''Drop_down_Auto_suggestive'''

# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.ID,"autosuggest").send_keys('ind')

'''Checkbox_static'''
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# dropdown = driver.find_element(By.XPATH,'//input[@id="checkBoxOption2"]')
# dropdown.click()
# assert dropdown.is_selected()


'''Checkbox_dynamic'''
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
# print(len(checkboxes))
# for checkbox in checkboxes:
#     if checkbox.get_attribute("id") == "checkBoxOption3":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break
#     time.sleep(2)

'''Radio Button'''

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.NAME,'radioButton').click()
assert driver.find_element(By.XPATH,'//input[@value="radio3"]').is_selected()
time.sleep(3)









