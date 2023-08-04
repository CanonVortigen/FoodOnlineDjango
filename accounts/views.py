from django.shortcuts import redirect, render
from accounts.models import User
from . forms import Userform
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        #print(request.POST)
        form = Userform(request.POST)
        if form.is_valid():
            # 1 - Create de User using de form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # 2 - Create de User using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']            
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been registered sucessfully')
            #print('User is created')
            return redirect('registerUser')
        else:
            print('Invalid Form')
            print(form.errors)
    else:
        form = Userform()

    context = {
        'form': form,
    }

    return render(request, 'accounts/registerUser.html', context)
