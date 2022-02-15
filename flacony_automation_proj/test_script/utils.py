""" this module contains utility function that are going to be used across proj """
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import accept_cookies,accept_cookies_cls, web_driver_path, main_url

# webdriver initialise
driver=webdriver.Chrome(web_driver_path)
driver.get(main_url)
driver.maximize_window()

def accept_all_cookies():
    """
    accept cookies
    :return:
    """
    time.sleep(10)
    root1 = driver.find_element(By.CSS_SELECTOR, accept_cookies)
    shadow_root1 = expand_shadow_element(root1)
    accept_all = shadow_root1.find_element(By.CSS_SELECTOR, accept_cookies_cls)
    accept_all.click()

def expand_shadow_element(element):
    """
    this function return expanded element from shadow dom
    :param element:
    :return:
    """
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

def get_web_ele_list(web_ele_path):
    """
    get web elements
    :param web_ele_path:
    :return:
    """
    sub_menu_ele = []
    for ele in web_ele_path:
        sub_menu_ele.append(driver.find_elements(By.XPATH,ele))
    return sub_menu_ele

def get_link_status(web_ele):
    """
    get link status
    :param web_ele:
    :return:
    """
    web_ele = get_web_ele_list(web_ele)
    for link in web_ele:
        if len(link) == 0:
            pass
        for links in link:
            r = requests.head(links.get_attribute('href'))
            print("Link {} is valid with http status code {}".format(links.get_attribute('href'),r.status_code))
