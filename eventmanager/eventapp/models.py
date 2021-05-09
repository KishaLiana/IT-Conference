from django.db import models

# Create your models here.

class Participants(models.Model): 

    choice = (
            ('Attendee', 'Attendee'),
            ('Speaker', 'Speaker'),
        )
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250) 
    phone = models.CharField(max_length=250)
    speaker = models.CharField(max_length=150, choices=choice,default='Attendee') 
    topic = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name 


class Program(models.Model): 
    name = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    speaker = models.ForeignKey(Participants,on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name


class Contact(models.Model): 
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField(max_length=250) 
    
    def __str__(self):
        return self.name
