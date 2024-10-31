# -*- coding: utf-8 -*-
from selenium import webdriver
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from selenium.webdriver.chrome.options import Options

FullTab = ""

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        chrome_options = Options()
        chrome_options.add_argument(
            r"--user-data-dir=C:\Users\kevin\AppData\Local\Google\Chrome\User Data")  # e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data C:\Users\kevin\AppData\Local\Google\Chrome\User Data
        chrome_options.add_argument(r'--profile-directory=Default')
        chrome_options.add_argument('--remote-debugging-pipe')
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument(r'--remote-debugging-port=1559')
        print("-3")
        #self.driver = webdriver.Chrome(executable_path=r"C:\Users\kevin\OneDrive\Desktop\ChromeDriver\chromedriver.exe", options=chrome_options)

        #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:1559")
        #self.driver = webdriver.Chrome(chrome_options)
        self.driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=r"C:\Users\kevin\OneDrive\Desktop\ChromeDriver\chromedriver.exe"),
                        options=chrome_options)
        print("1")

        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        print("2")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        global FullTab
        driver = self.driver
        driver.get(self.base_url + "chrome://newtab/")
        driver.get("https://ix.bdreporting.com/Home")
        driver.get("https://ix.bdreporting.com/NetWorth/Accounts/Tab/All")
        FullTab = driver.find_element("xpath",
            "//div[@id='react-app-bootstrapper']/div/section/article/div/article/section[2]/section/section[2]").text
        driver.get(self.base_url + "chrome://newtab/")
        driver.get("https://ix.bdreporting.com/Home")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
    print(FullTab)