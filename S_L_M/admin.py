from django.contrib import admin

from .models import Team,schudlematch,winmatch,score

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['id','Team_Name']
@admin.register(schudlematch)
class schudlematchAdmin(admin.ModelAdmin):
    list_display=['id','match_date','match_time']
@admin.register(winmatch)
class winmatchAdmin(admin.ModelAdmin):
    lis_display=['id','match','win_team']
@admin.register(score)
class scoreAdmin(admin.ModelAdmin):
    list_display=['id','match']




