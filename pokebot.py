import pokebase as pb
import random
from telegram.ext import Updater, CommandHandler
import requests
import re

def get_poke(id):
    poke = pb.pokemon(id)


    return poke

def get_random():
    id = random.randint(1,807)
    return id

def get_url():
    num = get_random()
    poke = get_poke(num)
    url = poke.sprites.front_default

    return url


def pokemon(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    if url != None:
        bot.send_photo(chat_id=chat_id, photo=url)
    else:
        bot.send_photo(chat_id=chat_id, photo='https://media.treasy.com.br/media/2015/11/nao-disponivel.jpg')

def main():
    updater = Updater('871112194:AAH8D41UYTbsNe6bQLdDfAJfbGEsPMOnDXY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pokemon',pokemon))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
