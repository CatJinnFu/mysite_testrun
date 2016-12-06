from django import forms

from . import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
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


