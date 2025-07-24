from django.db import models
from django.contrib.auth.models import User
class Team(models.Model):
    Team_Name=models.CharField(max_length=10)
    Team_city=models.CharField(max_length=15)
    Team_coach=models.CharField(max_length=15)
    members = models.ManyToManyField(User)
    def __str__(self):
        return self.Team_Name
class schudlematch(models.Model):
    First_team=models.ForeignKey(Team,related_name='First_team', on_delete=models.CASCADE)
    Second_team=models.ForeignKey(Team,related_name='second_team', on_delete=models.CASCADE)
    match_date=models.DateField(auto_now_add=False)
    match_time=models.TimeField(auto_now_add=False)
    def __str__(self):
        return f"{self.First_team} vs {self.Second_team} on {self.match_date}"
class winmatch(models.Model):
    match=models.ForeignKey(schudlematch, on_delete=models.CASCADE)
    Win_team=models.ForeignKey(Team, on_delete=models.CASCADE)
class score(models.Model):
    match=models.ForeignKey(schudlematch, on_delete=models.CASCADE)
    First_team=models.DecimalField(max_digits=5, decimal_places=0)
    second_team=models.DecimalField(max_digits=5, decimal_places=0)
    timestamp=models.TimeField(auto_now_add=True)
