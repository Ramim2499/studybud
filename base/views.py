from django.shortcuts import render



rooms = [
  {'id':1, 'name':'Lets learn Python!'},
  {'id':2, 'name':'Design with me'},
  {'id':3, 'name':'Front end developers'},
] 



def home(request):
  context = {'rooms':rooms}
  return render(request, 'base/home.html', context)
# {'how we want to specify it in the template':what we are passing in}


def room(request, pk):
  room = None
  for i in rooms:
    if i['id'] == int(pk):
      room = i

  context = {'room':room}
  return render(request, 'base/room.html', context)
