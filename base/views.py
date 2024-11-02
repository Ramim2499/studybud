from django.shortcuts import render
from .models import Room


# rooms = [
#   {'id':1, 'name':'Lets learn Python!'},
#   {'id':2, 'name':'Design with me'},
#   {'id':3, 'name':'Front end developers'},
# ]



def home(request):
  rooms = Room.objects.all #default model manager(objects) quary
  context = {'rooms':rooms}
  return render(request, 'base/home.html', context)
# {'how we want to specify it in the template':what we are passing in}


def room(request, pk):
  room = Room.objects.get(id=pk) #returns one single value using primary key
  context = {'room':room}
  return render(request, 'base/room.html', context)
