# pip install python-telegram-bot --upgrade
# conda install -c conda-forge python-telegram-bot

import telegram
import telegramToken as tToken

my_token = tToken.my_token
bot = telegram.Bot(token=my_token)  # bot 선언
updates = bot.getUpdates()  # update 내역을 받아옴
print(updates)

# for u in updates:
#     print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지의 chat id를 가져옵니다
to_name = bot.getUpdates()[-1].message.chat.first_name
print("char_id : {}, to_name : {}".format(chat_id, to_name))
bot.sendMessage(chat_id = chat_id, text=to_name+"님  저는 lovekhj_bot 입니다.")

print('telegram bot')

