from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  #flash message
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #saving the data, makes hashpass by own
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created for {username}! you are now able to login')  #flash message
            return redirect('login')
    else:
        form=UserRegisterForm()


    return render(request,'users/register.html',{'form': form})

#### Message-> typers #####
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error