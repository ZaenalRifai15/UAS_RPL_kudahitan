from django.shortcuts import render, redirect
from .models import Pengguna
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def index(request):
    return render(request, 'myapp/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pendaftaran berhasil!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            try:
                pengguna = Pengguna.objects.get(username=uname, password=pwd)
                request.session['id_pengguna'] = pengguna.id_pengguna
                messages.success(request, 'Login berhasil!')
                return redirect('home')  # ganti ke halaman dashboard
            except Pengguna.DoesNotExist:
                messages.error(request, 'Username atau password salah!')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logout berhasil.')
    return redirect('login')