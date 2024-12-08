from asgiref.sync import sync_to_async

import logging

from tg_bot.apps.bot.models import BotUser

logger = logging.getLogger(__name__)

@sync_to_async
def update_or_create_tg_user(object_user):
    telegram_id = object_user['id']
    full_name = object_user['full_name']
    username = object_user['username']

    telegram_user, create_status = BotUser.objects.update_or_create(telegram_id=telegram_id, full_name= full_name, username=username)
    if create_status is False:
        logger.info(f'Успешно обновлён user в БД {full_name} {username}')

    else:
        logger.info(f'Успешно создан user в БД {full_name} {username}')
    return create_status
