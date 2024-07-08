import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Firefox()
    driver.get("http://13.126.167.255:8088/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT,"Products").click()
    #driver.find_element(By.XPATH,"//span[text()='A-Factor']/parent::div/parent::div/following-sibling::div//button[text()='Add to Enquiry']").click()
    element = driver.find_element(By.XPATH,"//button[text()='Add to Enquiry']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    time.sleep(5)
    driver.save_screenshot(r"C:\screenshots\Enquiry.png")
    yield
    driver.close()

def test_validation_positive(setup):
    expected_url ="http://13.126.167.255:8088/products"
    current_url =driver.current_url
    assert expected_url == current_url ,"You are currently not in the Product Page"

def test_validation_negative(setup):
    expected_url = "http://13.126.167.255:8088/product"
    current_url = driver.current_url
    assert expected_url == current_url ,"You are currently not in the Product Page"

