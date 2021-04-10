from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/chatindex.html', {})


def room(request, room_name):
    name = {
        'room_name' : room_name
    }
    return render(request, 'chat/chatroom.html', name)
