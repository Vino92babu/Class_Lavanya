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
# driver.find_element(By.ID,"autosuggest").send_keys('ind')
# time.sleep(3)
# countries = driver.find_elements(By.XPATH,'//li[@class="ui-menu-item"]/a')
# print(len(countries))
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# assert driver.find_element(By.XPATH,'//input[@id="autosuggest"]').get_attribute("value") == "India"
# time.sleep(2)


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

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.NAME,'radioButton').click()
# assert driver.find_element(By.XPATH,'//input[@value="radio3"]').is_selected()
# time.sleep(3)

'''is_displayed --> use to find the elements is present on the page or not'''

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
# assert driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
# driver.find_element(By.XPATH,'//input[@id="hide-textbox"]').click()
# assert not driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()

'''Alerts'''
# Name = "Vinoth"
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("lavanya")
# driver.find_element(By.XPATH,'//input[@id="alertbtn"]').click()
# time.sleep(2)
# alerts = driver.switch_to.alert
# alerts_text = alerts.text
# print(alerts_text)
# assert not Name in alerts_text
# alerts.accept()
# time.sleep(2)
# driver.find_element(By.XPATH,'//input[@id="confirmbtn"]').click()
# time.sleep(1)
# alerts.dismiss()
# time.sleep(1)

'''Wait practice'''
'''Implicictly wait'''

'''Search the product'''
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
page_title = driver.title
assert page_title == "GreenKart - veg and fruits kart"
Search_box = driver.find_element(By.CSS_SELECTOR,'input[class="search-keyword"]')
Search_box.send_keys("be")
search_button = driver.find_element(By.CSS_SELECTOR,'button[class="search-button"]')
search_button.click()
time.sleep(3)




















