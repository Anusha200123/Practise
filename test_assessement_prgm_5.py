import time

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://13.126.167.255:8088/products")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='product-button']").click()
    yield driver



def get_actual_name(driver):
    return driver.find_element(By.TAG_NAME,"h1").text

def test_assert_Equal(setup):
    expected_name= "A-Factor"
    actual_name = get_actual_name(setup)
    assert actual_name == expected_name
    print("Chemical name is same ")

def test_assert_NotEqual(setup):
    expected_name = "AB-Factor"
    actual_name = get_actual_name(setup)
    assert actual_name != expected_name ,"Chemical name is not matching"

def test_assert_true(setup):
    expected_name = "A-Factor"
    actual_name = get_actual_name(setup)
    if actual_name == expected_name:
        assert True

def test_assert_false(setup):
    expected_name = "A-Factor"
    actual_name = get_actual_name(setup)
    if actual_name != expected_name:
        assert False

def test_assert_In():
    expected_name = "A-Factor"
    assert ("Factor" in expected_name)

def test_assert_Not_In():
    expected_name = "A-Factor"
    assert ("AB-Factor" not in expected_name)







