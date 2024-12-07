import telebot
import logging
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

from tg_bot.services.database.bot_user_uoc import update_or_create_tg_user

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')

telebot.logger.setLevel(settings.LOG)

logger = logging.getLogger(__name__)



# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
async def send_welcome(message):

    telegram_id = message.json['from']['id']
    first_name = message.json['from']['first_name']
    last_name = message.json['from']['last_name']
    full_name = f'{first_name} {last_name}'
    username = message.json['from']['username']
    object_user = {'id':telegram_id,
                   'full_name':full_name,
                   'username':username,
                   }
    try:
        await update_or_create_tg_user(object_user)
    except Exception as err:
        logger.info(f'при добавление user появилась ошибка {err}')
    text = 'Бот запомнил тебя :)'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)