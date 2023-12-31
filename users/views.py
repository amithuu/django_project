from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, UserProfileForm

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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form  = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile
                                 )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, ' Account Details has been Updated! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)
    

    context ={
                'u_form' : u_form,
                'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)