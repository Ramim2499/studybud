from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Topic > Room >
class Topic(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)#if the topic parent class is deleted the room child model is not deleted null = True allowed in the database
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True) #it can be blank by null=True, blank=True means the submitted form can also be true
  participants = models.ManyToManyField(User, related_name='participants', blank=True)
  updated = models.DateTimeField(auto_now=True) #takes the time when every time the save method is called
  created = models.DateTimeField(auto_now_add=True) #only take the time when we first save or create this instance(initial time)

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.name #it will return the name of the class in the admin panel



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #the User model is defined in default
    room = models.ForeignKey(Room, on_delete=models.CASCADE)#(parent name(Room) many to one relationship, value when the parent model(Room) is deleted the child model(Message) is also deleted)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
      return self.body[0:50]

class Course_Teacher(models.Model):
  name = models.CharField(max_length=200)
  designation = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name

class Team_member_Info(models.Model):
  name = models.CharField(max_length=200)
  Student_id = models.CharField(max_length=10, null=True, blank=True)
  contribution = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name
