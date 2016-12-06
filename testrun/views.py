from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
from .models import Transaction
from .models import Card_Type
from .models import Client
from .models import Staff

def index(request):
    latest_transaction_list = Transaction.objects.order_by('-date_created')
    #template = loader.get_template('testrun/index.html')
    #output = ''',\r\n '''.join([str(t) for t in latest_transaction_list])
    context = {'latest_transaction_list': latest_transaction_list,}
    return render(request, 'testrun/index.html', context)


def client(request):
    client_list = Client.objects.all()

    context = {'client_list': client_list,}
    return render(request, 'testrun/client.html', context)

def client_add(request):
    client = models.Client()

    if request.POST['client']:
        client.client_name = request.POST['client']
        client.save()

    client_list = Client.objects.all()
    context = {'client_list': client_list,}    

    return render(request, 'testrun/client.html', context)   

def client_delete(request, client_pk=0):
    client= get_object_or_404(models.Client, pk=client_pk)
    client.delete()

    client_list = Client.objects.all()
    context = {'client_list': client_list,}    

    return render(request, 'testrun/client.html', context)

def card(request):
    card_list = Card_Type.objects.all()

    context = {'card_list': card_list,}
    return render(request, 'testrun/card.html', context) 

def card_add(request):
    card = Card_Type()

    if request.POST['card']:
        card.type = request.POST['card']
        card.save()

    card_list = Card_Type.objects.all()
    context = {'card_list': card_list,}    

    return render(request, 'testrun/card.html', context)

def card_delete(request, card_pk=0):
    card = get_object_or_404(models.Card_Type, pk=card_pk)
    card.delete()

    card_list = Card_Type.objects.all()
    context = {'card_list': card_list,}    

    return render(request, 'testrun/card.html', context)



def staff(request):    
    staff_list = Staff.objects.all()

    context = {'staff_list': staff_list,}
    return render(request, 'testrun/staff.html', context) 

def staff_add(request):
    staff = Staff()

    if request.POST['staff']:
        staff.staff_name = request.POST['staff']
        staff.save()

    staff_list = Staff.objects.all()

    context = {'staff_list': staff_list,}  

    return render(request, 'testrun/staff.html', context)


def staff_delete(request, staff_pk=0):
    staff = get_object_or_404(models.Staff, pk=staff_pk)
    staff.delete()

    staff_list = Staff.objects.all()
    context = {'staff_list': staff_list,}    

    return render(request, 'testrun/staff.html', context)

def search(request):	
	if request.POST['search']:
		value = request.POST['search']
		latest_transaction_list = Transaction.objects.filter(amount__contains=value)
	else:
		latest_transaction_list = Transaction.objects.order_by('-date_created')	

	context = {'latest_transaction_list': latest_transaction_list,}
	return render(request, 'testrun/index.html', context)


def detail(request, transaction_pk):
	transaction = get_object_or_404(Transaction, pk=transaction_pk)
	return render(request, 'testrun/detail.html', {'transaction': transaction})
    #return HttpResponse("You're looking at transaction %s." % transaction_id)    

def results(request, transaction_pk):
	transaction = get_object_or_404(Transaction, pk=transaction_pk)
	
	try:
		if request.POST['processed'] == 'True':
			transaction.processed = True
		else:
			transaction.processed = False
	except:
		transaction.processed = False
		transaction.save()
		
	else:	
		transaction.save()
	#response = "You're looking at the results of transaction %s."
	latest_transaction_list = Transaction.objects.filter(pk=transaction_pk)
	context = {'latest_transaction_list': latest_transaction_list,}
	return render(request, 'testrun/index.html', context)


def transaction_edit(request, transaction_pk=0):
    transaction = get_object_or_404(models.Transaction, pk=transaction_pk)
    card_list = Card_Type.objects.all()
    client_list = Client.objects.all()
    staff_list = Staff.objects.all()
    form = forms.TransactionForm()
    
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Transaction added!")
            return HttpResponseRedirect(reverse('testrun:transaction_edit', kwargs={
                'transaction_pk': transaction_pk,  }))
    return render(request, 'testrun/transaction_edit.html', {'form': form, 
                                                             'transaction' : transaction, 
                                                             'card_list' : card_list, 
                                                             'client_list' : client_list,
                                                             'staff_list' : staff_list
                                                             }) 	


def transaction_create(request):
    
    transaction = models.Transaction
    card_list = Card_Type.objects.all()
    client_list = Client.objects.all()
    staff_list = Staff.objects.all()
    form = forms.TransactionForm()
    
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            transact = form.save(commit=False)
            transact.transaction = transaction
            transact.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Transaction added!")
            return HttpResponseRedirect(reverse('testrun:transaction_create'))
    return render(request, 'testrun/transaction_form.html', {'form': form, 
                                                             'transaction' : transaction,
                                                             'card_list' : card_list, 
                                                             'client_list' : client_list,
                                                             'staff_list' : staff_list
                                                             }) 