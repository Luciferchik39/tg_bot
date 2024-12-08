from asgiref.sync import sync_to_async
import datetime
import logging

from tg_bot.apps.bot.models import work_stats

logger = logging.getLogger(__name__)

@sync_to_async
def create_and_add_ticket(message):
    full_name = message['full_name']
    id_ticket = message['id_ticket']
    current_date_time = datetime.datetime.now()
    count_ticket = 1

    ticket, create_status = work_stats.objects.get_or_create(full_name=full_name, id_ticket=id_ticket, time_of_addition=current_date_time, count_ticket=count_ticket)
    if create_status is False:
        logger.info(f'Успешно обновлён ticket в БД {full_name}')
    else:
        logger.info(f'Успешно создан user в БД {full_name} ')
    return create_status


