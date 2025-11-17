from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {"user_form": user_form})

def login_view(request):
    if request.method == "POST":
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            # Log the user in
            from django.contrib.auth import login
            user = auth_form.get_user()
            if user is not None:    
                login(request, user)
                return redirect('cars_list')
            else:
                return redirect('login')
    else:
        auth_form = AuthenticationForm()
    return render(request, 'login.html', {"auth_form": auth_form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')


