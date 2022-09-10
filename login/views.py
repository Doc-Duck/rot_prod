from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import LoginForm


def login_page(request):
    form = LoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            if request.user.is_staff:
                print('doctor')
                return redirect('doctor_page')
            else:
                print('patient')
                return redirect('doctor_page')

    return render(request, 'login/login.html', context=context)