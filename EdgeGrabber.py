# -*- coding: utf-8 -*-
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.edge.options import Options
from itertools import islice
import unittest, time, re
tab =""

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        subprocess.call(r"taskkill /F /im msedge.exe")
        time.sleep(5)
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        edge_options = Options()
        edge_options.add_argument(
            r"--user-data-dir=C:\Users\kevin\AppData\Local\Microsoft\Edge\User Data")
        edge_options.add_argument(r'--profile-directory=Default')
        self.driver = webdriver.Edge(options=edge_options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        global tab
        driver = self.driver
        driver.get(self.base_url + "edge://newtab//")
        driver.get("https://ix.bdreporting.com/Home")
        driver.find_element(By.XPATH,"//a[contains(text(),'Net Worth')]").click()
        driver.get("https://ix.bdreporting.com/NetWorth/Accounts")
        driver.find_element(By.XPATH,"//a[contains(text(),'Accounts')]").click()
        tab = driver.find_element(By.CSS_SELECTOR,
            "section.ix-account-page-layout-content.ix-networth-account-list.ix-account-page-layout-content--card").text
        driver.back()
        driver.back()

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
        splittab = tab.splitlines()[8:]
        tablist = []
        for i in range(0, len(splittab),6):
            tablist.append(splittab[i:i+6])

        #print(tablist)

        with open(r"C:\\Users\kevin\OneDrive\Desktop\BSVal.csv", "w") as f:
            for acct in tablist:
                acctcode = acct[0]
                acctval = acct[3].replace(',', '')
                acctdate = acct[4] if acct[5] == '--' else acct[5]
                print(f'{acctcode},{acctval},{acctdate}', file=f)

        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    print('go')
    unittest.main()
