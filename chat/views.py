from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index2.html', {})


def room(request, room_name):
    name = {
        'room_name' : room_name
    }
    return render(request, 'chatroom.html', name)

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
                    return render(request, 'chat/user_signup.html/#login')
            else:
                messages.info(request, 'Password Input Empty')
                return redirect('UserSignup')
        else:
            messages.info(request, 'Username Input Empty')
            return redirect('UserSignup')
    else:
        return render(request, "chat/user_Signup.html/#signup")
