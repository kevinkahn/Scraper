# -*- coding: utf-8 -*-
import subprocess

#import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.edge.options import Options
from itertools import islice
import time, re
tab =""

#class AppDynamicsJob(unittest.TestCase):
class GrabData():
    #@staticmethod
    #def close_edge_gracefully():
    #   for proc in psutil.process_iter(['pid', 'name']):
    #        if proc.info['name'] == 'msedge.exe':
    #            proc.terminate()  # Sends a termination signal

    def setUp(self):
        #self.close_edge_gracefully()
        #subprocess.call(r"taskkill /im msedge.exe")
        subprocess.run(r"taskkill /F /im msedge.exe", capture_output=True)
        time.sleep(2)
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        edge_options = Options()
        edge_options.add_argument(
            r"--user-data-dir=C:\Users\kevin\AppData\Local\Microsoft\Edge\User Data")
        edge_options.add_argument(r'--profile-directory=Default')
        self.driver = webdriver.Edge(options=edge_options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        #self.verificationErrors = []
        #self.accept_next_alert = True

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

    def tearDown(self):
        splittab = tab.splitlines()[8:]
        tablist = []
        for i in range(0, len(splittab),6):
            tablist.append(splittab[i:i+6])

        with open(r"C:\\Users\kevin\Desktop\BSVal.csv", "w") as f:
            for acct in tablist:
                acctcode = acct[0]
                acctval = acct[3].replace(',', '')
                acctdate = acct[4] if acct[5] == '--' else acct[5]
                print(f'{acctcode},{acctval},{acctdate}', file=f)

if __name__ == "__main__":
    print('go')
    G = GrabData()
    G.setUp()
    G.test_app_dynamics_job()
    G.tearDown()
