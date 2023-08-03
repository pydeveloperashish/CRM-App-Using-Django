from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Records

# Create your views here.
def home(request):
    records = Records.objects.all()
    
    # check to see if the user is logged in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, "You have been authenticated...")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again...")
            redirect('home')
            
    context = {'records': records}        
    return render(request, 'home.html', context = context)


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # check if user already exists
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, 
                                password = password)
            if user:
                login(request, user)
                messages.success(request, 'User Registration Successful...')
                return redirect('home')
        else:
            context = {'form': form}             
            return render(request, 'register.html', context = context)    
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context = context)


def customerRecord(request, pk):
    if request.user.is_authenticated:
        # look up customer record
        customerRecord = Records.objects.get(id = pk)
        context = {'customerRecord': customerRecord}
        return render(request, 'record.html', context = context)
    else:
        messages.success(request, 'You must be Logged in to view that page...')
        return redirect('home')
    
    
def deleteRecord(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You must be Logged in to do that...')
        return redirect('home')