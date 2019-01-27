from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import unittest
import  time
from selenium.webdriver import  Chrome, ChromeOptions

class test_FirstTest(unittest.TestCase):
        def setUp(self):
            opts = ChromeOptions()
            opts.add_experimental_option("detach", True)

            self.driver = webdriver.Chrome('C:/Users/medbo/Downloads/chromedriver_win32/chromedriver.exe',options=opts)
            self.driver.get("https://accounts.google.com")

        def test_LoginIn(self):
            driver = self.driver
            email = driver.find_element_by_xpath("//div/input")
            email.send_keys('medvedepam@gmail.com')
            nextbut = driver.find_element_by_id("identifierNext")
            nextbut.click()
            time.sleep(1)
            password = driver.find_element_by_xpath("//div/input")
            password.send_keys("qscesz123")
            submbut = driver.find_element_by_id("passwordNext")
            submbut.click()
            acept = "https://myaccount.google.com/?pli=1"
            time.sleep(2)
            self.assertEqual(self.driver.current_url, acept, "Invalid page")

        def test_IncLogIn(self) :
            driver = self.driver
            email = driver.find_element_by_xpath("//div/input")
            email.send_keys('some@gmail.com')
            nextbut = driver.find_element_by_id("identifierNext")
            nextbut.click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//div[contains(text(), 'Не вдалоfся знайти ваш обліковий запис Google')]")
            except NoSuchElementException:
                print('Test fall')
                return False
            return True

        def tearDown(self):
            self.driver.quit()

if  __name__ == "__main__":
        unittest.main()



