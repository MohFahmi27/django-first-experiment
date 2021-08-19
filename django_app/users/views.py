from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}, Go ahead and Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, template_name='users/register.html', context={'form': form})


@login_required
def profile(request) -> HttpResponse:
    return render(request, template_name='users/profile.html', context={'title': 'Profile'})
