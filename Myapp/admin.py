from django.contrib import admin

# Register your models here.
from Myapp.models import Team, Player, GameScore

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(GameScore)