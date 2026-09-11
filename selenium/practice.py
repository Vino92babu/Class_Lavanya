from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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
# time.sleep(3)

# validating on product displayed

expected_list = ['Cucumber - 1 Kg','Beetroot - 1 Kg','Beans - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list = [ ]
total_list = driver.find_elements(By.XPATH,'//h4[@class="product-name"]')
for list in total_list:
    actual_list.append(list.text)
print(actual_list)
assert expected_list == actual_list

# Validating the number of product count should be > 0
total_products = driver.find_elements(By.CSS_SELECTOR,'div[class="product"]')
total_products_count = len(total_products)
print("total_products_count: ",total_products_count)
assert total_products_count > 0

# validate the number of product count with len of total_products_count
count = 0
for product in total_products:
    product.find_element(By.XPATH,'.//div[@class="product-action"]/button').click()
    count = count+1
print("count :",count)
assert count == total_products_count
# time.sleep(2)

# validating item_count == count == total_product_count and click an add to cart btn and proceed with ceckout btn

item = driver.find_element(By.XPATH,'//tbody/tr[1]/td/strong')
item_count = int(item.text)
print("item_count :", item_count)
assert item_count == count == total_products_count
cart_btn = driver.find_element(By.CSS_SELECTOR,'img[alt="Cart"]')
cart_btn.click()
chk_out_btn = driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]')
chk_out_btn.click()

# explicitly_wait_adding

apply_promo_text = driver.find_element(By.CSS_SELECTOR,".promoCode")
apply_promo_text.send_keys("rahulshettyacademy")
apply_btn = driver.find_element(By.CSS_SELECTOR,".promoBtn")
apply_btn.click()
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
succ_promo_text = driver.find_element(By.CSS_SELECTOR,".promoInfo")
print(succ_promo_text.text)
assert succ_promo_text.text == "Code applied ..!"

# Table Validation

total_price = driver.find_elements(By.XPATH,'//td[5]/p[@class="amount"]')
total_sum = 0
for total_item_price in total_price:
    price = int(total_item_price.text)
    total_sum = total_sum + price
print(total_sum)


