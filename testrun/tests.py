from django.test import TestCase

# Create your tests here.
from testrun.models import Transaction

class TrasactionMethodTests(TestCase):
	def SetUp(Self):
		Transaction.objects.create(date=timezone.now(),
								   card_type = 'AMEX',
								   company = 'OfficeWorks',
								   purchase_details = 'binders and pencils',
								   client = "Aruba",
								   notes = "n/a",
								   amount = 1050.50,
								   GST='inc GST',
								   staff = 'Dieter',
								   comments = '.',
								   processed = False)	
	