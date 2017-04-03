from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
	dob = models.DateField('Date Of Birth')
	branch = models.CharField(max_length=200)
	red_rose = models.IntegerField(default=0)
	yellow_rose = models.IntegerField(default=0)
	year = models.IntegerField(default=1)
	def __str__(self):
		return self.user.username

class Message(models.Model):
	to = models.ForeignKey(User, related_name='to_user_profile')
	frm = models.ForeignKey(User, related_name='from_user_profile')
	message = models.CharField(max_length=1000)
	def __str__(self):
		return self.message

class RoseRecord(models.Model):
	to = models.ForeignKey(User, related_name='to_user')
	frm = models.ForeignKey(User, related_name='from_user')
	def __str__(self):
		return self.to.username
class YellowRoseRecord(models.Model):
	to = models.ForeignKey(User, related_name='to_user_yellow')
	frm = models.ForeignKey(User, related_name='from_user_yellow')
	def __str__(self):
		return self.to.username