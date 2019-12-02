from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request,"login_app/login_page.html")

def register_users(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST["email"],password=request.POST["password"],confirm_password=request.POST['confirm_password'])
        new_user = User.objects.last()
        request.session['user_first'] = new_user.first_name
        
        request.session['user_id'] = new_user.id

        return redirect("/fav_book")

def login_user(request):
    if request.method == "POST":
        errors = User.objects.basic_login(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['user_first'] = user.first_name
            request.session['user_last'] = user.last_name
            

        return redirect("/fav_book")

def success(request):
    if 'user_first' in request.session:
        return render(request,"login_app/success.html")
    else:
        return redirect ("/")

def clear(request):
    request.session.flush()
    return redirect('/')

def admin(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "login_app/admin.html", context)