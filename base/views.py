from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm



def home(request):
  rooms = Room.objects.all #default model manager(objects) quary
  context = {'rooms':rooms}
  return render(request, 'base/home.html', context)
# {'how we want to specify it in the template':what we are passing in}


def room(request, pk):
  room = Room.objects.get(id=pk) #returns one single value using primary key
  context = {'room':room}
  return render(request, 'base/room.html', context)

def createRoom(request):
  form = RoomForm()

  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  context = {'form':form}
  return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)

  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save()
      return redirect('home')

  context = {'form':form}
  return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
  room = Room.objects.get(id=pk)
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  return render(request, 'base/delete.html', {'obj':room})