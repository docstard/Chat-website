from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User, Group
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request, 'mysite/index2.html')
    


def userSignup(request):
    if request.method == 'POST':
        username = request.POST['signupusername']
        password = request.POST['signuppassword']
        if username is not None:
            if password is not None:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Taken')
                    return redirect('UserSignup')

                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return render(request, 'mysite/user_signup.html')
            else:
                messages.info(request, 'Password Input Empty')
                return redirect('UserSignup')
        else:
            messages.info(request, 'Username Input Empty')
            return redirect('UserSignup')
    else:
        return render(request, "mysite/user_Signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Sorry, your username or password was incorrect.')
            return redirect('Login')
    
    else:
        return render(request, 'mysite/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def volSignup(request):
    if request.method == 'POST':
        username = request.POST['signupusername']
        password = request.POST['signuppassword']
        if username is not None:
            if password is not None:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Taken')
                    return redirect('Volsignup')

                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return render(request, 'mysite/Vsignup.html/#login')
            else:
                messages.info(request, 'Password Input Empty')
                return redirect('Volsignup')
        else:
            messages.info(request, 'Username Input Empty')
            return redirect('Volsignup')
    else:
        return render(request, "mysite/Vsignup.html")