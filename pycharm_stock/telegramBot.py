# pip install python-telegram-bot --upgrade
# conda install -c conda-forge python-telegram-bot

import telegram
import jackToken as tToken

def send_telegram_bot(send_msg):
    # print('telegrambot : ' , send_msg)

    my_token = tToken.telegram_my_token
    bot = telegram.Bot(token=my_token)  # bot 선언

    bot.sendMessage(chat_id=tToken.telegram_chat_id, text = send_msg)

    # print('telegram bot')

if __name__ == "__main__":
    send_telegram_bot("telegrambot main test")
