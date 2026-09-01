from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


'''Browser's url'''
def browser_demo(url):
    driver.get(url)
    driver.maximize_window()

'''input text'''
def login_demo():
    browser_demo("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID,"password").send_keys("Learning@830$3mK2")

# login_demo()


'''Dropdown'''
# Static

def dropdown_static_demo():
    browser_demo("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID,"password").send_keys("Learning@830$3mK2")
    Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_value("teach")
    Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_index(0)
    Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')
dropdown_static_demo()).select_by_visible_text("Consultant")
