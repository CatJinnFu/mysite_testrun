from django import forms

from . import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        #date_created = forms.TextInput(attrs={'disabled':'disabled'})
        fields = [
        	'date_created',
			'date_transaction', 
			'card_type', 
			'supplier', 
			'purchase_details', 
			'amount',  
			'GST', 
			'client',
			'wfm_job_number',
			'staff', 
			'notes', 
			'processed' 
        ]

        def __init__(self, *args, **kwargs):
        	super(TransactionForm, self).__init__(*args, **kwargs)
        	instance = getattr(self, 'instance', None)
        	if instance and instance.pk:
       			self.fields['date_created'].widget.attrs['disabled'] = True
