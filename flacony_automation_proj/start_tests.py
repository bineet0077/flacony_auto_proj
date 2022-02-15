import time
from test_script.utils import driver
from test_script import test_get_link_status, test_add_item_to_cart

def start_test():
    """
    function to test the given use cases
    :return:
    """
    # get link status of main menu
    test_get_link_status.get_main_menu_link_status()
    time.sleep(10)
    print("-"*15,"test case to get main menu link status is done","-"*15)
    # get link status of make up sub menu
    test_get_link_status.get_makeup_sub_menu_link_status()
    time.sleep(10)
    print("-" * 15, "test case to get main menu link status is done", "-" * 15)
    # validate invalid coupon messgae
    test_add_item_to_cart.check_coupon_code_message()
    print("-" * 15, "test case to get coupon message validation is done", "-" * 15)
    print("=" * 15, "ALL TEST CASES EXECUTED", "=" * 15)
    driver.close()
    driver.quit()
if __name__ == '__main__':
    start_test()
