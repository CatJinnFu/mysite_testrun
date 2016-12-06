from django.contrib import admin

# Register your models here.
from .models import Transaction
from .models import Card_Type
from .models import Client
from .models import Staff

admin.site.register(Transaction)
admin.site.register(Card_Type)
admin.site.register(Client)
admin.site.register(Staff)