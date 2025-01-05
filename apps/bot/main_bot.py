import telebot
import logging
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from telebot import types
from tg_bot.services.database.bot_user_uoc import update_or_create_tg_user, \
    user_find
from tg_bot.services.database.create_and_add_ticket import \
    create_and_add_ticket, add_ticket_pass_ticket

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')

telebot.logger.setLevel(settings.LOG)

logger = logging.getLogger(__name__)



# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    key_bord = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='+1 решённый тикет в копилку')
    btn2 = types.KeyboardButton(text='Получить колличество решённых тикетов за сегодня')
    btn3 = types.KeyboardButton(text='Инфо')
    key_bord.add(btn1, btn2, btn3)


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
    await bot.reply_to(message, text, reply_markup=key_bord)



def work(message):
    return 'https://supchat.taxi.yandex-team' in message.text

@bot.message_handler(func= work)
async def start(message):
    try:
        user_pk = await user_find(message.json['from']['id'])
    except Exception as err:
        logger.info(f'проблемы при поиске юзера в БД {err}')
        await bot.send_message(message.chat.id, message.json['text'])
    first_name = message.json['from']['first_name']
    last_name = message.json['from']['last_name']
    full_name = f'{first_name} {last_name}'
    id_ticket = message.json['text']
    object_ticket = {'id_ticket': id_ticket,
                   'full_name': full_name,
                     'user_pk': user_pk
                     }
    try:
        b = await create_and_add_ticket(object_ticket)
        if b:
            await bot.send_message(message.chat.id, text='Тикет добавлен 🎉')
        else:
            await bot.send_message(message.chat.id, text='этот тикет ты уже добавлял бро 🥴')
    except Exception as err:
        logger.info(f'проблемы с добавлением тикета {err}')
        await bot.send_message(message.chat.id, message.json['text'])

def add_tick(message):
    return '+1 решённый тикет в копилку' in message.text
@bot.message_handler(func=add_tick)
async def add_ticket(message):
    try:
        user_pk = await user_find(message.json['from']['id'])
    except Exception as err:
        logger.info(f'проблемы при поиске юзера в БД {err}')
        await bot.send_message(message.chat.id, message.json['text'])
    first_name = message.json['from']['first_name']
    last_name = message.json['from']['last_name']
    full_name = f'{first_name} {last_name}'
    id_ticket = 'Pass'
    object_ticket = {'id_ticket': id_ticket,
                     'full_name': full_name,
                     'user_pk': user_pk
                     }
    try:
        b = await add_ticket_pass_ticket(object_ticket)
        if b:
            await bot.send_message(message.chat.id, text='Тикет добавлен 🎉')
    except Exception as err:
        logger.info(f'проблемы с добавлением тикета {err}')
        await bot.send_message(message.chat.id, message.json['text'])

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)