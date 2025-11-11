from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def index(request) :
    return render ( request, 'index.html' )


def about(request) :
    return render ( request, 'about.html' )


def company(request) :
    return render ( request, 'company.html' )


def contact(request) :
    return render ( request, 'contact.html' )


def design(request) :
    return render ( request, 'design.html' )


def news(request) :
    return render ( request, 'news.html' )

# def SignIn(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         user = authenticate(request, email=email, password=password)
#         if user:
#             login(request, user)
#             return redirect('index')