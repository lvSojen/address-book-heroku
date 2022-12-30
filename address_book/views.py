from django.shortcuts import render, redirect

def home(request) :
    return render(request, 'pages/home.html', {})

def add_address(request) :
    return render(request, 'address/add_address.html', {})