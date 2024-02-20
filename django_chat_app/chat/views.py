from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Chat, Message
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    if request.method == "POST":
        mychat = Chat.objects.get(id=1)
        new_message = Message.objects.create(
            text=request.POST["textmessage"],
            chat=mychat,
            author=request.user,
            receiver=request.user,
        )
       
        serialized_message = serializers.serialize("json", [new_message])
        return JsonResponse(serialized_message[1:-1], safe=False)
    chat_messages = Message.objects.filter(chat__id=1).order_by("created_at")
    return render(request, "chat/index.html", {"messages": chat_messages})


def login_view(request):
    if request.method == "POST" and "accept" in request.POST:
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return HttpResponseRedirect("/chat")
        else:
            return render(request, "auth/login.html", {"wrongPassword": True})
    elif "redirect_to_signup" in request.POST:
        return HttpResponseRedirect("/signup")
    return render(request, "auth/login.html")




def signup(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            if User.objects.filter(username=username).exists():
                return render(request, "auth/sign_up.html", {"user_exists": True, "username": username})
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/chat")
        except ValueError:
            return render(request, "auth/sign_up.html", {"emptyField": True})
    return render(request, "auth/sign_up.html")




def logout_view(request):
    logout(request)
    return redirect('/login')


