""" module to verify invalid coupon submit response """
import time
from test_script.utils import driver, accept_all_cookies
from config.config import expected_message, perfume, perfume_item,\
    add_to_cart, nav_to_cart, vcode, vinput, btn_submit, invalid_c_msg

def check_coupon_code_message():
    """
    fun to validate invaild coupon message
    displayed in web page
    :return:
    """
    try:
        driver.find_element_by_xpath(perfume).click()
        time.sleep(5)
        driver.find_element_by_xpath(perfume_item).click()
        time.sleep(5)
        driver.find_element_by_xpath(add_to_cart).click()
        time.sleep(5)
        driver.find_element_by_xpath(nav_to_cart).click()
        time.sleep(5)
        driver.find_element_by_xpath(vinput).send_keys(vcode)
        time.sleep(5)
        driver.find_element_by_xpath(btn_submit).click()
        time.sleep(5)
        text_message = driver.find_element_by_xpath(invalid_c_msg).text
        print("expected message is {} and out put messgae is {}".format(expected_message, text_message))
        time.sleep(5)
        assert text_message == expected_message
    except Exception as err:
        print(err)