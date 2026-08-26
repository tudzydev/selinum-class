import unittest
import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bmi(unittest.TestCase):
    def setUp(self):
        options = Options()

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_bmi_input(self):
        height_cm  = 183
        weight_kg = 103

        self.driver.get("https://www.khonkaenram.com/th/services/health-information/health-articles/checkup-and-vaccine/program-bmi")

        # input
        weight_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "weight"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", weight_input, str(weight_kg))
        
        height_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "height"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", height_input, str(height_cm))

        # click calculate
        calculate_btn = self.wait.until(
            EC.presence_of_element_located((By.ID, "calculateBtn"))
        )
        self.driver.execute_script("arguments[0].click();", calculate_btn)

        #expected bmi   
        height_meter = height_cm / 100.0
        expected_bmi = weight_kg / (height_meter ** 2)
        expected_bmi_text_2d = f"{expected_bmi:.2f}"

        # wait result
        bmi_result_input = self.wait.until(
            lambda driver: driver.find_element(By.ID, "bmiResult")
        )
        
        self.wait.until(
            lambda driver: bmi_result_input.get_attribute("value") == expected_bmi_text_2d
        )

        bmi_val = bmi_result_input.get_attribute("value")
        meaning_val = self.driver.find_element(By.ID, "meaningResult").get_attribute("value")

        # verify bmi
        self.assertEqual(
            bmi_val,
            expected_bmi_text_2d,
            f"BMI ไม่ถูกต้อง: คาดหวัง {expected_bmi_text_2d} แต่ได้ {bmi_val}"
        )

        # verify category
        if expected_bmi < 18.5:
            expected_category = "คุณผอมเกินไป ควรเพิ่มน้ำหนัก"
        elif expected_bmi < 25.0:
            expected_category = "คุณอยู่ในเกณฑ์ปกติ"
        elif expected_bmi < 30.0:
            expected_category = "คุณเริ่มอ้วน ควรออกกำลังกาย"
        elif expected_bmi <= 40.0:
            expected_category = "คุณอ้วนมาก ควรลดน้ำหนัก"
        else:
            expected_category = "คุณอ้วนขั้นสูงสุด !!!"

        self.assertEqual(
            meaning_val,
            expected_category,
            f"Category ไม่ใช่ {expected_category}"
        )

        print("--------------------------------")
        print("Browser : Chrome")
        print(f"Height  : {height_cm}")
        print(f"Weight  : {weight_kg}")
        print(f"BMI     : {bmi_val}")
        print(f"Meaning : {meaning_val}")
        print("Status  : TEST PASSED")
        print("--------------------------------")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()