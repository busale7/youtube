from django.db import models
from django.contrib.auth.models import User #importing User from models

# Create your models here.
class Channel(models.Model): 
	#number_subscribers = models.IntegerField(auto_increment_for('user'))
	number_subscribers=models.PositiveIntegerField()
	name = models.CharField(max_length=125)
	creator =models.ForeignKey(User, default=1,on_delete=models.CASCADE)
	def __str__(self):
		return self.name


class Video(models.Model): 
	name= models.CharField(max_length=125)
	description =models.TextField()
	channel =models.ForeignKey(Channel, default=1,on_delete=models.CASCADE)
	video_link =models.URLField()
	def __str__(self):
		return self.name

'''class ChannelFollowers(models.Model): 
	user= models.ForeighKey(User, unique=True)
	date=models.DateTimeField(auto_now_add=True)
	count =models.IntegerField(default=1)
	subscribers=models.ManyToManyField(Channel, related_name='subscribers')
	def __str__(self):
		return '%S, %S' % self.user, self.count'''
