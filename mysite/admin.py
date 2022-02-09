from django.contrib import admin
from mysite.models import Game, GameUser

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ('name', 'gid', 'timestamp', 'bank')

@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
    fields = ('game', 'name', 'money')
