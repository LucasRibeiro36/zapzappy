import zapzappy
import time
import wikipedia
bot = zapzappy.Whatsapp_api()
wikipedia.set_lang("pt")
while not bot.take_screenshot():
    print("Waiting qrcode")
time.sleep(5)
while True:
    for chat in bot.get_new_Messages():
        msg_base = chat['msg']['text']
        chat_array = msg_base.split(' ')
        if chat['msg']['text'] == "/start":
            bot.send_Message(chat['msg']['id'], 'hello world')
        elif chat_array[0] == '/wiki':
            try:
                msg = chat['msg']['text']
                print(msg.replace('/wiki', ''))
                busca = wikipedia.page(msg.replace('/wiki ', ''))
                print(busca)
                busca_msg = f"WIKIPEDIA\n{busca.title}\n{busca.content}"
                bot.send_Message(chat['msg']['id'], busca_msg)
            except:
                bot.send_Message(chat['msg']['id'], "Não existe")