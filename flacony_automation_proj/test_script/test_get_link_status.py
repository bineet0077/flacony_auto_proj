""" this module is to check all submenu link available for make up menu and main menu"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config.config import web_ele_path_for_main_menu
from test_script.utils import driver, accept_all_cookies,get_link_status
from config.config import makeup_menu, web_ele_path_for_makeup_menu

# accepting cookies
accept_all_cookies()

def get_main_menu_link_status():
    """
    func to get main menu links status
    :return:
    """
    try:
        get_link_status(web_ele_path_for_main_menu)
    except Exception as err:
        print(err)

def get_makeup_sub_menu_link_status():
    """
    func to get makeup sub menu status
    :return:
    """
    try:
        element_to_hover_makeup_sub_menu_link = driver.find_element(By.XPATH,makeup_menu)
        hover = ActionChains(driver).move_to_element(element_to_hover_makeup_sub_menu_link)
        hover.perform()
        get_link_status(web_ele_path_for_makeup_menu)
    except Exception as err:
        print(err)