from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # -> it will create a new form with the data in it.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for the {username}!, Please Login')
            return redirect('login')
    else:
        form = UserRegisterForm()  #-> if it is not post we create a blank form
    return render(request, 'users/register.html', {'form':form})
