from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#username
user_name = "username"
#password
password = "password"
#get the instagram page
driver = webdriver.Chrome(executable_path=r"C:\Users\Charl\Desktop\chromedriver.exe")
driver.get("https://www.instagram.com/")
sleep(3)
#action class declaration
actions = ActionChains(driver)
element = driver.find_element_by_class_name("f0n8F ")
element.send_keys(user_name)
#get the elements
element = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label")
element.send_keys(password)
element.send_keys(Keys.RETURN)
sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
#actions.click(on_element = element1).perform()
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
sleep(2)

elem = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button").click()
driver.execute_script("window.scrollTo(0,1000)")
driver.close()
