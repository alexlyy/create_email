import selenium
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import robot



def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=6):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)

#information to change
prenom = "yourname"
nom = "yoursurname"
mail = prenom + nom + "1465756"
mdp = "password"
birth_day = '01'
birth_year = '0000' #change it
#options = poptions()
url = "https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-en&flowName=GlifWebSignIn&flowEntry=SignUp"
phone = '0000000000'

driver = webdriver.Safari()



driver.get(url)
#send info to url
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input').send_keys(prenom)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input').send_keys(nom)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(mail)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(mdp)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(mdp)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="phoneNumberId"]').send_keys(phone)
#time.sleep(5)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="code"]').click()
#time.sleep(5)

#Move automatically the mouse to the code 

action = webdriver.common.action_chains.ActionChains(driver)

action.click()
action.perform()

#action = ActionChains(driver)
#action.click().perform()
#new page number + date of birth

# driver.find_element_by_xpath('//*[@id="day"]').send_keys(birth_day)
# month = driver.find_element_by_xpath('//*[@id="month"]')
# month.get(1).click() #click on january
# driver.find_element_by_xpath('//*[@id="year"]').send_keys(birth_year)

# gender = driver.find_element_by_xpath('//*[@id="gender"]')
# gender.get(1).click() #click on january

# driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()


