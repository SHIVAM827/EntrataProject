import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#####################################################################
# Purpose:This test case check the navigation of different pages
######################################################################

def test_navigation():
    driver.get("https://www.entrata.com/")
    assert "Entrata" in driver.title

    # clicking on Accept Cookies option if visible and maximizing the window
    driver.maximize_window()
    driver.find_element("id","rcc-confirm-button").click()
    time.sleep(5)

    # Navigating to different pages
    # Navigating to Solutions pages
    driver.find_element("xpath"," //div[text()='Solutions' and @class='main-nav-link' ]").click()
    time.sleep(5)
    assert "Property Management Software | Entrata" in driver.title

    # Navigating to #Navigating to Solutions pages pages
    driver.find_element("xpath", " //div[text()='Products' and @class='main-nav-link' ]").click()
    time.sleep(5)
    assert "Property Management Software | Entrata" in driver.title

    # Navigating to Resources pages
    driver.find_element("xpath", " //a[@class='main-nav-link' and text()='Resources']").click()
    time.sleep(5)
    assert "Helpful Resources for the Multifamily Industry" in driver.title

    # Closing the window
    driver.close()


#####################################################################
# Purpose:This test case verifies that dynamic content is loaded on the home page
######################################################################

def test_dynamic():
    driver.get("https://www.entrata.com/")
    assert "Entrata" in driver.title

    # clicking on Accept Cookies option if visible and maximizing the window
    driver.find_element("id","rcc-confirm-button").click()
    driver.maximize_window()
    time.sleep(5)

    # Verify that dynamic content is loaded
    dynamic_element = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='hero-left']")))
    assert dynamic_element.text != ""
    driver.close()


#####################################################################
# Purpose:This test case validates the search functionality by performing a search and verifying the presence of search results.
######################################################################

def test_search_functionality():
    driver.get("https://www.entrata.com/")
    assert "Entrata" in driver.title

    # clicking on Accept Cookies option if visible and maximizing the window
    driver.find_element("id","rcc-confirm-button").click()
    driver.maximize_window()
    time.sleep(5)

    # Perform a search
    search_input = driver.find_element("xpath","//a[text()='Message Center' and @class = 'standard-footer-link']")
    search_input.send_keys("Message Center")
    driver.execute_script("window.find('" + "Message Center" + "')")

    # Verify search results
    search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
    (By.XPATH, "//a[text()='Message Center' and @class = 'standard-footer-link']")))
    assert len(search_results) > 0
    driver.quit()


#####################################################################
# Purpose:This test case Tests the contact form functionality by filling out the form fields without submitting the form
######################################################################

def test_contact_form():
    driver.get("https://www.entrata.com/")
    assert "Entrata" in driver.title

    # clicking on Accept Cookies option if visible and maximizing the window
    driver.find_element("id","rcc-confirm-button").click()
    driver.maximize_window()

    # Clicking on Watch Demo Button
    driver.find_element("xpath","//a[@class='button-default solid-dark-button' and text()='Watch Demo']").click()
    time.sleep(5)

    # Filling out contact form
    firstname_input = driver.find_element("name","FirstName")
    firstname_input.send_keys("John Doe")

    lastname_input = driver.find_element("name","LastName")
    lastname_input.send_keys("tran")

    email_input = driver.find_element("name","Email")
    email_input.send_keys("john.doe@example.com")

    company_input = driver.find_element("name","Company")
    company_input.send_keys("abc.")

    phoneno_input = driver.find_element("name","Phone")
    phoneno_input.send_keys("9745++++++")

    unitcount_input = driver.find_element("name","Unit_Count__c")
    unitcount_input.send_keys("1-10")

    jobtitle_input = driver.find_element("name","Title")
    jobtitle_input.send_keys("Engineer")

    # Closing the window (without submitting the form as informed )
    driver.close()


