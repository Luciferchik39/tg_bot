from asgiref.sync import sync_to_async
import datetime
import logging

from tg_bot.apps.bot.models import work_stats

logger = logging.getLogger(__name__)

@sync_to_async
def create_and_add_ticket(message):
    user_pk = message['user_pk']
    full_name = message['full_name']
    id_ticket = message['id_ticket']
    current_date_time = datetime.datetime.now()
    count_ticket = 1

    ticket, create_status = work_stats.objects.get_or_create(full_name=full_name, id_ticket=id_ticket, time_of_addition=current_date_time, count_ticket=count_ticket, user_pk_id=user_pk)
    if create_status is False:
        logger.info(f'Успешно обновлён ticket в БД {full_name}')
    else:
        logger.info(f'Успешно создан ticket в БД {full_name} ')
    return create_status

@sync_to_async
def add_ticket_pass_ticket(message):
    user_pk = message['user_pk']
    full_name = message['full_name']
    id_ticket = message['id_ticket']
    current_date_time = datetime.datetime.now()
    count_ticket = 1
    ticket = work_stats.objects.create(full_name=full_name, id_ticket=id_ticket, time_of_addition=current_date_time, count_ticket=count_ticket, user_pk_id=user_pk)
    if ticket is False:
        logger.info(f'что пошло не так при добавление ticket в БД')
    else:
        logger.info(f'Успешно создан ticket в БД')
    return ticket


@sync_to_async
def show_ticket(message):
    user_pk = message['user_pk']
    current_date_time = datetime.datetime.now()
    count = work_stats.objects.filter(time_of_addition=current_date_time, user_pk_id=user_pk).count()

    if count is False:
        logger.info(f'0 тикетов по заданным параметрам')
    else:
        logger.info(f'тикеты успешно посчитаны')
    return count
