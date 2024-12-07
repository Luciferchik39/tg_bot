from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group
from django.db.models import ManyToOneRel

from tg_bot.apps.bot.models import BotUser, work_stats

admin.site.unregister(User)
admin.site.unregister(Group)

def get_fields_for_model(db_model):
    fields = []
    '''так делать не рекомендуется, почему узнаю позже :)'''
    for field in db_model._meta.get_fields():
        if isinstance(field, ManyToOneRel):
            continue
        fields.append(field.name)
    return fields

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(BotUser)
    search_fields = ['username', 'full_name', 'telegram_id']


@admin.register(work_stats)
class work_statsAdmin(admin.ModelAdmin):
    list_display = get_fields_for_model(work_stats)
    search_fields = ['id_ticket', 'id_ticket']

