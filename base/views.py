from django.shortcuts import render, redirect
from .mail_sender import sender
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser
email = ""
code = ""
def menu(request):
    if request.method == "GET":
        try:
            user = request.session.get('user')
            print(CustomUser.check_password(user.password, CustomUser.objects.get(username=user.login).password))
            user = authenticate(username=user.login, password=user.password)
            print(user)
        except:
            pass
        dic = {"is_auth": request.user.is_authenticated}

        return render(request, "menu.html", dic)
    elif request.method == "POST":
        return redirect('http://127.0.0.1:8000/registration')


def register(request):
    global email
    global code
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = CustomUser.objects.create_user(login, email, password)
        user.last_name = "Bukich"
        user.save()

        #code = sender(email)
        request.session['user'] = request.POST
        dic = {"is_auth": user.is_authenticated}
        print("-------------------------------")
        return redirect('http://127.0.0.1:8000')
    elif request.method == "GET":
        return render(request, "registr.html")

def confirm(request):
    if request.method == "GET":
        return render(request, "confirm.html")
    elif request.method == "POST":
        print(code)
        if code == request.POST.get("code"):
            return render(request, "Вы зарегистрированы")
        else:
            return render(request,"Неправильный код")

def authentificate(request):
    if request.method == "GET":
        if request.session["user_id"] == -999:
            print("isn't authentificate")
        else:
            print("authentificated")
        return render(request, "confirm.html")
    elif request.method == "POST":
        #request.session["user_id"] = user.objects.get(id == 3, -999)
        request.session.modified = True
        return render(request, "confirm.html")