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
        #options.add_argument("--headless")
        options.add_argument("--user-data-dir=data_chrome")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--disable-gpu")
        options.add_extension('./extensions/extension_1_7_0_0.crx')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        self.driver.get("https://web.whatsapp.com/")
        sleep(3.0)
    def take_screenshot(self):
            try:
                qr_code = self.driver.find_element(By.CSS_SELECTOR, '._3jid7 > canvas:nth-child(3)')
                qr_code.screenshot('./qrcode.png')
                sleep(10)
            except:
                pass
            try:
                self.driver.find_element_by_css_selector("div._2_1wd.copyable-text.selectable-text")
                return True
            except:
                return False
    def send_Message(self,number,message):
        try:
            user = self.driver.find_element_by_xpath(f"//span[@title='{number}']")
            user.click()
            text = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').text
            if text != '':
                chat = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
                chat.send_keys(Keys.ENTER)
                if message.find("\n"):
                    for line in message.split("\n"):
                        chat.send_keys(line)
                        chat.send_keys(Keys.SHIFT + Keys.ENTER)
                    chat.send_keys(Keys.ENTER)
                else:
                    chat.send_keys(message)
                    chat.send_keys(Keys.ENTER)
                return True
            else:
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
    def get_new_Messages(self):
        chats = []
        messages = []
        for number in range(30):
            try:
                if int(self.driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._1SjZ2 > div._15smv > span:nth-child(1) > div > span').text) >= 1: 
                    chats.append(self.driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._2pkLM > div._3Dr46 > span').text)
                    messages.append(self.driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._1SjZ2 > div._2vfYK > span > span._35k-1._1adfa._3-8er').text)
            except:
                pass
        return chats,messages

        
    def quit(self):
        self.driver.quit()



"""def get_new_Messagens():
        chats = []
        messages = []
        for number in range(30):
            try:
                if int(driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._1SjZ2 > div._15smv > span:nth-child(1) > div > span').text) >= 1: 
                    chats.append(driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._2pkLM > div._3Dr46 > span').text)
                    messages.append(driver.find_element_by_css_selector(f'#pane-side > div:nth-child(1) > div > div > div:nth-child({number}) > div > div > div.TbtXF > div._1SjZ2 > div._2vfYK > span > span._35k-1._1adfa._3-8er').text)
            except:
                pass
        return chats,messages

teste = get_new_Messagens()
for i in range(0,1):
    for j in range(0,30):
        try:
            print(teste[i][j])
            print(teste[i+1][j])
        except:
            pass"""