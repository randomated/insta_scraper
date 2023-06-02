from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time

class InstagramScraper:
  def __init__(self, is_headless=True, logger=None, saver=None):
    self.logger = logger
    self.saver = saver

    options = FirefoxOptions()
    options.add_argument('-no-sandbox')
    options.add_argument('-disable-dev-shm-usage')
    options.add_argument('-private')

    if is_headless:
      options.add_argument('-headless')

    self.driver = webdriver.Firefox(options=options)

  def start(self, links):
    # try:
    #   self.__login()
    # except LinkCannotProcessException as e:
    #   self.__log_file(f"LOGIN: {e}")
    # else:

    for link in links["scrape_list"]:
      time.sleep(10)
      try:
        self.__log_file(f"STARTING: {link['link']}")
        self.driver.get(link["link"])
        self.__process(link["stores"])
      except LinkCannotProcessException as e:
        self.__log_file(f"An exception occurred in link({link['link']}): {e}")
      else:
        self.__log_file(f"No exception occurred in link({link['link']})")

  def close(self):
    self.driver.quit()

  def __login(self):
    self.driver.get("https://www.instagram.com/")
    time.sleep(5)
    try:
      username_input = self.__find_element(self.driver, By.CSS_SELECTOR, 'input[name="username"]', None, 10, 5, "username_input")
      username_input.send_keys("randomateddd")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    time.sleep(5)
    try:
      password_input = self.__find_element(self.driver, By.CSS_SELECTOR, 'input[name="password"]', None, 10, 5, "password_input")
      password_input.send_keys("hello@1234")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    time.sleep(5)
    try:
      submit_button = self.__find_element(self.driver, By.CSS_SELECTOR, 'button[type="submit"]', None, 10, 5, "submit_button")
      submit_button.click()
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    time.sleep(5)
    try:
      self.__find_element(self.driver, By.XPATH, "//*[contains(text(), 'Not Now')]", None, 10, 5, "Not Now")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

  def __process(self, stores):
    time.sleep(10)
    user_agent = self.driver.execute_script("return navigator.userAgent;")
    self.__log_file(f"User-Agent: {user_agent}")

    elements_to_find = self.__first_insta_type()
    try:
      last_element = None
      for locator_type, locator, exception_name in elements_to_find:
        time.sleep(5)
        try:
          if exception_name == "first second_element":
            time.sleep(10)

          if exception_name == "Follow":
            self.__find_element(self.driver, locator_type, locator, None, 10, 5, exception_name)
          else:
            if last_element is None:
              last_element = self.__find_element(self.driver, locator_type, locator, None, 10, 5, exception_name)
            else:
              last_element = self.__find_element(self.driver, locator_type, locator, last_element, 10, 5, exception_name)
        except TimeoutException as e:
          raise TimeoutException(e.msg)
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")
    else:
      try:
        link_tag = self.__find_element(self.driver, By.XPATH, './/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a', None, 10, 5, "a tag")
      except TimeoutException as e:
        raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

      new_link = link_tag.get_attribute('href')
      self.driver.get(new_link)
      time.sleep(10)

      try:
        # Multiple image
        next_button = self.__find_element(self.driver, By.XPATH, "//button[@aria-label='Next']", None, 10, 5, "next button")
      except TimeoutException as e:
        try:
          # Single image
          image_tag = self.__find_element(self.driver, By.XPATH, './/main/div/div[1]/div/div[1]/div/div/div/div/div/div/div[1]/img', None, 10, 5, "img tag")
        except TimeoutException as ee:
          raise LinkCannotProcessException(f"Cannot find element error: {ee.msg} -- {e.msg}")
        else:
          h1_text = self.__find_element(self.driver, By.XPATH, './/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/div/li/div/div/div[2]/div[1]/h1', None, 10, 5, "h1 text")
          images = []
          images.append(image_tag.get_attribute('src'))

          self.__save_data(new_link, h1_text.text, images, stores)
      else:
        h1_text = self.__find_element(self.driver, By.XPATH, './/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/div/li/div/div/div[2]/div[1]/h1', None, 10, 5, "h1 text")
        images = []
        has_button = True
        while has_button:
          ul_tag = self.__find_element(self.driver, By.XPATH, './/main/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/ul', None, 10, 5, "ul tag")
          img_elements = ul_tag.find_elements(By.XPATH, ".//img")
          for img_element in img_elements:
            src = img_element.get_attribute("src")
            if src not in images:
              images.append(src)

          try:
            next_button = self.__find_element(self.driver, By.XPATH, "//button[@aria-label='Next']", None, 10, 2, "next button")
            next_button.click()
          except TimeoutException as e:
            has_button = False

        self.__save_data(new_link, h1_text.text, images, stores)

  def __find_element(self, driver, locator_type, locator, parent_element=None, timeout=10, max_tries=5, code_line=""):
    for i in range(max_tries):
      try:
        if parent_element is None:
          element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator))
          )
          return element
        else:
          element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator)), parent_element
          )
          return element
      except TimeoutException:
        self.__log_file(f"Timed out waiting for element ({i + 1}/{max_tries}). (line {code_line})")
    raise TimeoutException(f"Element not found after {max_tries} tries. (line {code_line})")
  
  def __first_insta_type(self):
    elements_to_find = [
        (By.XPATH, "//*[contains(text(), 'Follow')]", "Follow"),
        (By.TAG_NAME, 'main', "first main_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first second_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first third_element"),
        (By.CSS_SELECTOR, 'article:first-child', "first fourth_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first fifth_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first sixth_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first seventh_element"),
        (By.CSS_SELECTOR, 'div:first-child', "first eighth_element"),
    ]
    return elements_to_find

  def __log_file(self, message):
    if self.logger is None:
      print(message)
    else:
      self.logger.log(message)

  def __save_data(self, new_link, h1_text, images, stores):
    if self.saver is None:
      print(f"{new_link} - {h1_text} - {images}")
    else:
      inserted_id = self.saver.add_scraped_data(h1_text, new_link, images)

      for store in stores:
        self.saver.add_store(inserted_id, store['store_name'], store['wls_id'])

class LinkCannotProcessException(Exception):
  pass

# if __name__ == '__main__':
#   links = ["https://www.instagram.com/lululemonjp/", "https://www.instagram.com/bluebottlejapan/?hl=ja", "https://www.instagram.com/reebokjp/", "https://www.instagram.com/nanga_official/", "https://www.instagram.com/venex_jp/"] #, "https://www.instagram.com/urthcaffe_japan/?hl=ja", "https://www.instagram.com/brownrice_tokyo/", "https://www.instagram.com/biocafe_shibuya_official/", "https://www.instagram.com/rinatokitchen/", "https://www.instagram.com/ko.so.cafe/", "https://www.instagram.com/kitchen_watarigarasu/", "https://www.instagram.com/jingumaelakanka/", "https://www.instagram.com/mominokihouse_official/", "https://www.instagram.com/no.501.bottletokyo/", "https://www.instagram.com/fabudine/", "https://www.instagram.com/happy_hour2020/", "https://www.instagram.com/abio_farms_market/", "https://www.instagram.com/ficoandpomum/?ref=badge", "https://www.instagram.com/terraburgerandbowl/", "https://www.instagram.com/greenbrothers025/"]
#   scraper = InstagramScraper(False)
#   scraper.start(links)
#   scraper.close()