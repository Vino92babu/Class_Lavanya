from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
# driver.find_element(By.NAME,"name").send_keys("Vinoth")
# driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
# # driver.find_element(By.ID,"exampleInputPassword1").send_keys("Admin123")
# driver.find_element(By.CSS_SELECTOR,'input[placeholder="Password"]').send_keys("Admin123")

,click()


'''
Syntax : //tagname[@attribute = "value]

//input[@placeholder="Password"]


Locating with respect to elements and attributes

1) Loacting element with known attribute. 
ex: //*[@placeholder="Password"]

2) Locating element with known tagname & Attribute
ex: //input[@placeholder="Password"]

3) Locating Elements with visible text [Exact match]
ex: //div[text()="Name is required"]

4) Locating Elements with visible text [partial match]
ex: //div[contains(text(),"req")]

5) locating elements with multiple attribute
ex: //label[@class="form-check-label"][@for="inlineRadio2"][text()="Employed"]

6) Locating elenment when starting visible text is known
ex: // //div[starts-with(text(),"N")]


Locating elements relative to known elements. 

1) Locationg a parent element
ex: //input[@name="email"]/parent::div/parent::form

2) Locationg a child element
ex: //input[@name="email"]/parent::div/parent::form/child::div[1]/child::input[@name="name"]

3) Locating following element
ex: //input[@name="email"]/following::div[1]

4) Locating preceding elenment
ex: //input[@name="email"]/preceding::div[@class="container"]/child::div

5) Locating with Following-slibling
ex: //input[@name="email"]/parent::div/parent::form/child::div/following-sibling::div[5]

6) Locating with preceding-slibling
ex: //input[@name="email"]/parent::div/parent::form/child::div/following-sibling::div[5]/preceding-sibling::div

'''


