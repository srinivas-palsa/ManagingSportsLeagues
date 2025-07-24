from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.db.models import Max, Subquery, OuterRef
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team,schudlematch,score,winmatch
from .forms import TeamCreateForm,schudlematchCreateForm,ScoreCreateForm
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def user_dash(request):
    return render(request,'Usports.html')
def Team_create(request):
    if request.method == 'POST':
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TeamCreateForm()
    return render(request,'team.html',{'form': form})
def New_schedules(request):
    if request.method == 'POST':
        form = schudlematchCreateForm(request.POST)
        if form.is_valid():
            match_date = request.POST['match_date']
            match_time = request.POST['match_time']
            First_team = form.cleaned_data['First_team']
            Second_team = form.cleaned_data['Second_team']
            data =schudlematch.objects.create(First_team=First_team,Second_team=Second_team,match_date=match_date,match_time=match_time)
            data.save()
            return redirect('home') 
    else:
        form = schudlematchCreateForm()
    return render(request,'schedule.html',{'form': form})
def Update_scores(request):
    if request.method == 'POST':
        form = ScoreCreateForm(request.POST)
        if form.is_valid():
            match=form.cleaned_data['match']
            First_team=form.cleaned_data['First_team']
            second_team=form.cleaned_data['second_team']
            exist = score.objects.filter(match=match).first()
            if exist:
                exist.First_team=First_team
                exist.second_team=second_team
                exist.save()
                return redirect('home')
        else:
            Score=score.objects.create(
                match=match,
                First_team=First_team,
                second_team=second_team,
            )
            Sore.save()
            return redirect('home') 
    else:
        form = ScoreCreateForm()
    return render(request,'scores.html',{'form': form})
def user_actions(request):
    return render(request,'useractions.html')
def view_Team(request):
    data =Team.objects.all()
    return render(request,'useractions.html',{'Teams':data})
def match_schudles(request):
    data=schudlematch.objects.all()
    return render(request,'useractions.html',{'matches':data})
def Track_score(request):
    data = score.objects.all()
    return render(request,'useractions.html',{'scores':data})
def contact_view(request):
    data=True
    return render(request,'useractions.html',{'contact':data})
def manage_users(request):
    users=User.objects.all()
    return render(request,'manageuser.html',{'users':users})
