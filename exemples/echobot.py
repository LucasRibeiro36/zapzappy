import zapzappy
import time
bot = zapzappy.Whatsapp_api()
while not bot.take_screenshot():
    print("Waiting qrcode")
time.sleep(5)
while True:
    chats = bot.get_new_Messages()
    for i in range(0,1):
        for j in range(0,30):
            try:
                chat = chats[i][j]
                msg = chats[i+1][j]
                bot.send_Message(chat,f"{chat}:{msg}")
            except:
                pass

