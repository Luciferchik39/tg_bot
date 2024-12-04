import telebot
import logging
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')

telebot.logger.setLevel(settings.LOG)

logger = logging.getLogger(__name__)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Поздравим Илюшу :)'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)