from django import forms
from .models import Team,schudlematch,score
class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['Team_Name', 'Team_city', 'Team_coach', 'members']
class schudlematchCreateForm(forms.ModelForm):
    class Meta:
        model = schudlematch
        fields = ['First_team', 'Second_team',]
class ScoreCreateForm(forms.ModelForm):
    class Meta:
        model = score
        fields = ['match', 'First_team','second_team']