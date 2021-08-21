from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Coffee, Espresso
import datetime
from .forms import EspressoForm

# Create your views here.
def index(request):
    coffees = Coffee.objects.all()
    espresso_logs = Espresso.objects.all().order_by("-timestamp")
    month = datetime.datetime.now()
    current_month = month.strftime("%B")
    context = {
        "coffees": coffees,
        "current_month": current_month,
        "espresso_logs": espresso_logs
    }
    return render(request, "calibration/index.html", context)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Passwords must match
        if not password == confirmation:
            messages.error(request, "Passwords did not match")
            return redirect("register")

        # Attemp to create User
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.warning(request, "Username taken")
            return redirect("register")
        login(request, user)
        return redirect("index")
    else:
        return render(request, "calibration/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username and/or password")
            return redirect("login")
    else:
        return render(request, "calibration/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "GET":
        context = {
            "user": user
        }
        return render(request, "calibration/profile.html", context)
    else:
        
        new_username = request.POST["username"]
        new_email = request.POST["email"]

        #  preserve old field and make sure new fields are not empty stirngs
        if new_username == "" or new_username == user.username:
            pass
        else:
            user.username = new_username
            
        if new_email == "" or new_email == user.email:
            pass
        else:
            user.email = new_email

        user.save()
        return redirect("profile", user_id=user.id)

@login_required
def espresso_log(request):
    context = {
        "form": EspressoForm()
    }
    if request.method == "GET":
        return render(request, "calibration/espresso_log.html", context)
    else:
        form = EspressoForm(request.POST)
        user = User.objects.get(id=request.user.id)

        if form.is_valid():
            espresso = form.save(commit=False)
            espresso.save()
            espressos = Espresso.objects.all()
            messages.success(request, "Log added successfully")
            return redirect("index")
        else:
            return render(request, "calibration/espresso_log.html", {"form": EspressoForm()})
        

    





