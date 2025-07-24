from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_login_view,name='Admin'),
    path('Register',views.Register_view,name='register'),
    path('create-Team',views.Team_create,name='Teamview'),
    path('create-schudles',views.New_schedules,name='Scheduldes'),
    path('update-scores',views.Update_scores,name='Scores'),
    path('actions',views.user_actions,name='actions'),
    path('Teams-view',views.view_Team,name='teams_view'),
    path('matches-view',views.match_schudles,name='matches_view'),
    path('scores-view',views.Track_score,name='score_view'),
    path('contact',views.contact_view,name='contact'),
    path('Manage-users',views.manage_users,name='Manage_user'),
    #path('',views.,name=''),

]