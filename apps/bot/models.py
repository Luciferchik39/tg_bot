from django.db import models

# Create your models here.

class BotUser(models.Model):
    """Пользователи бота"""
    telegram_id = models.PositiveBigIntegerField(('ID Telegram'), db_index=True, unique=True)
    full_name = models.CharField(('Полное имя'), max_length=250,blank=True, null=False)
    username = models.CharField(('Username'), max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'



class work_stats(models.Model):
    full_name = models.CharField(('Полное имя'), max_length=250, blank=True, null=False)
    id_ticket = models.CharField(('ID Переоформленного тикета'), max_length=250, blank=True, null=True)
    data_add = models.DateField(('Дата добавления тикета'))
    count_ticket = models.IntegerField(('Колличество'), null=False,)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'