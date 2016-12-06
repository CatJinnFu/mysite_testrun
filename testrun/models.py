from django.db import models
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponseRedirect
# Create your models here.
class Transaction(models.Model):
	date_created = models.DateTimeField(default=timezone.now())
	date_transaction = models.CharField(max_length=200,default='dd/mm/yy' )
	card_type = models.CharField(max_length=200)
	supplier = models.CharField(max_length=200)
	purchase_details = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=99999999,decimal_places=2)
	GST = models.CharField(max_length=100,default='inc GST')
	client = models.CharField(max_length=255)
	wfm_job_number = models.CharField(max_length=255,default='001')
	staff = models.CharField(max_length=255,default='')
	notes = models.TextField()
	processed = models.BooleanField(default=False)

	   

	def __str__(self):
		if self.processed == True:
			process = 'Processed'
		else:	
			process = ''

		return "{} -- {} -- {} -- {} -- ${} -- {} -- {} ".format(
													 self.date_created.strftime("%d/%m/%Y"),
													 self.card_type,
													 self.supplier,
													 self.purchase_details,
													 self.amount,
													 self.staff,
													 process)


class Card_Type(models.Model):		
		type = models.CharField(max_length=200)



		def __str__(self):
			return "{}" .format(self.type)


class Client(models.Model):		
		client = models.CharField(max_length=200)
		client_name = models.CharField(max_length=200,default='')



		def __str__(self):
			return "{}" .format(self.client)

class Staff(models.Model):		
		staff = models.CharField(max_length=200)
		staff_name = models.CharField(max_length=200, default='')



		def __str__(self):
			return "{}" .format(self.staff)