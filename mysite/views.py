from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html', {})


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
                    return render(request, 'mysite/user_signup.html/#login')
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
        return render(request, 'main/login.html')