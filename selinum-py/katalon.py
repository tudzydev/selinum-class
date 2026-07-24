# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KatalonBmi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_katalon_bmi(self):
        driver = self.driver
        driver.get("https://www.calculator.net/bmi-calculator.html")
        driver.find_element(By.ID, "cage").click()
        driver.find_element(By.ID, "cage").clear()
        driver.find_element(By.ID, "cage").send_keys("50")
        driver.find_element(By.ID, "ckg").clear()
        driver.find_element(By.ID, "ckg").send_keys("100")
        driver.find_element(By.NAME, "x").click()
        driver.get("https://www.calculator.net/bmi-calculator.html?cage=50&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=180&ckg=100&printit=0&ctype=metric&x=Calculate")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
