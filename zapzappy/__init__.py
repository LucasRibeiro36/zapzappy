from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

class Whatsapp_api:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--user-data-dir=data_chrome")
        options.add_argument("--start-maximized")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=OFF")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        self.driver.get("https://web.whatsapp.com/")
        sleep(3.0)
    def take_screenshot(self):
            try:
                ele = self.driver.find_element(By.CSS_SELECTOR, '._3jid7 > canvas:nth-child(3)')
                ele.screenshot('./qrcode.png')
            except:
                pass
            try:
                self.driver.find_element_by_css_selector("div._2_1wd.copyable-text.selectable-text")
                return True
            except:
                return False
    def send(self,number,message):
        try:
            user = self.driver.find_element_by_xpath(f"//span[@title='{number}']")
            user.click()
            chat = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
            if message.find("\n"):
                for line in message.split("\n"):
                    chat.send_keys(line)
                    chat.send_keys(Keys.SHIFT + Keys.ENTER)
                chat.send_keys(Keys.ENTER)
            else:
                chat.send_keys(message)
                chat.send_keys(Keys.ENTER)
            return True
        except:
            return False
    def quit(self):
        self.driver.quit()