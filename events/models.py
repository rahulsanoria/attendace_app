from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone 
from django.db import models 

class Person(models.Model):
	name  = models.CharField(max_length = 100)
	roll_no = models.CharField(max_length = 100 , unique = True)
	email = models.CharField(max_length = 200)
	phone  = models.CharField(max_length = 15 , blank = True , null = True)
	
	def __str__(self):
		return self.roll_no



class Attendance(models.Model):
	person = models.ForeignKey(Person)
	subject1 = models.CharField(max_length = 200,null = True)
	subject2 = models.CharField(max_length = 200,null = True)
	subject3 = models.CharField(max_length = 200,null = True)
	subject4 = models.CharField(max_length = 200,null = True) 
	subject5 = models.CharField(max_length = 200,null = True)
	# subject6 = models.CharField(max_length = 200)

	def __str__(self):
		return self.person				