from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check to see if the user is logged in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, "You have been authenticated")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again...")
            redirect('home')
    return render(request, 'home.html', context = {})

def loginUser(request):
    pass

def logoutUser(request):
    pass

