import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# Test in browser Chrome.

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_wordpress_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_chrome, 5)

        print(driver_chrome.title)
        print(driver_chrome.current_url)
        print(driver_chrome.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_chrome.title
        if not "California Real Estate" in driver_chrome.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_chrome.find_element(By.TAG_NAME, "img").get_attribute("src"))

        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_chrome.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_chrome.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_chrome.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_chrome.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        (driver_chrome.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_chrome.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        driver_chrome.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_chrome.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        time.sleep(1)

    def test_search_wordpress_chrome_1120x550(self):                 # Другой размер окна 1120x550.
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_chrome, 5)
        print(driver_chrome.title)
        print(driver_chrome.current_url)
        print(driver_chrome.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_chrome.title
        if not "California Real Estate" in driver_chrome.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_chrome.find_element(By.TAG_NAME, "img").get_attribute("src"))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_chrome.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_chrome.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_chrome.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_chrome.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        print(driver_chrome.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_chrome.find_element(By.XPATH, '//button[@type="submit"]').click()
        driver.implicitly_wait(5)
        driver_chrome.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_chrome.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()  # Close the browser Chrome.  Закрваем браузер Chrome.


# Test in browser Firefox..


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_wordpress_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_firefox, 5)

        print(driver_firefox.title)
        print(driver_firefox.current_url)
        print(driver_firefox.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_firefox.title
        if not "California Real Estate" in driver_firefox.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_firefox.find_element(By.TAG_NAME, "img").get_attribute("src"))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_firefox.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_firefox.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_firefox.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_firefox.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        print(driver_firefox.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_firefox.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        driver_firefox.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_firefox.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        time.sleep(1)

    def test_search_wordpress_firefox_1120x850(self):                 # Другой размер окна 1120x850.
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 850)
        driver_firefox.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_firefox, 5)
        print(driver_firefox.title)
        print(driver_firefox.current_url)
        print(driver_firefox.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_firefox.title
        if not "California Real Estate" in driver_firefox.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_firefox.find_element(By.TAG_NAME, "img").get_attribute("src"))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_firefox.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_firefox.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_firefox.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_firefox.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        print(driver_firefox.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_firefox.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        driver_firefox.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_firefox.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser Firefox.


# Test in browser Edge.

class EdgeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_search_wordpress_Edge(self):
        driver_Edge = self.driver
        driver_Edge.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_Edge, 5)

        print(driver_Edge.title)
        print(driver_Edge.current_url)
        print(driver_Edge.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_Edge.title
        if not "California Real Estate" in driver_Edge.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_Edge.find_element(By.TAG_NAME, "img").get_attribute("src"))

        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_Edge.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_Edge.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_Edge.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_Edge.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_Edge.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        (driver_Edge.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_Edge.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        driver_Edge.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_Edge.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser Edge. Закрваем браузер Edge.


# Test in browser Opera.

class OperaSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Opera()
        self.driver.maximize_window()

    def test_search_wordpress_Opera(self):
        driver_Opera = self.driver
        driver_Opera.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver_Opera, 5)

        print(driver_Opera.title)
        print(driver_Opera.current_url)
        print(driver_Opera.find_element(By.LINK_TEXT, "California Real Estate"))
        assert "California Real Estate" in driver_Opera.title
        if not "California Real Estate" in driver_Opera.title:
            raise Exception("Title for California Real Estate page is wrong!")
        print(driver_Opera.find_element(By.TAG_NAME, "img").get_attribute("src"))

        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-55"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-34"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-56"]')))
        wait.until(ES.visibility_of_element_located((By.XPATH, '//*[@class="wp-image-30"]')))
        print(driver_Opera.find_element(By.XPATH, '//*[text()="Send Us a Message"]'))
        (driver_Opera.find_element(By.NAME, "g2-name").send_keys("Sergei"))
        (driver_Opera.find_element(By.NAME, "g2-email").send_keys("abc@gmail.com"))
        (driver_Opera.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Message"))
        driver_Opera.execute_script("window.scrollTo(document.body.scrollDown, 50000)")
        (driver_Opera.find_element(By.TAG_NAME, "button").get_attribute("type"))
        driver_Opera.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        driver_Opera.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        driver_Opera.find_element(By.XPATH, '//a[contains(text(),"Home")]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser Opera. Закрываем браузер Opera.


if __name__ == "__main__":
    unittest.main()
