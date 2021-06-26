import zapzappy
import time
bot = zapzappy.Whatsapp_api()
while not bot.take_screenshot():
    print("Waiting qrcode")
time.sleep(5)
while True:
    chats = bot.get_new_Messages()
    for chat in chats:
        bot.send_Message(chat['msg']['id'], chat['msg']['text'])

