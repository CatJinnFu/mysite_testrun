from django.conf.urls import url

from . import views

app_name = 'testrun'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<transaction_pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<transaction_pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<transaction_pk>[0-9]+)/transaction_edit/$', views.transaction_edit, name='transaction_edit'),
   	url(r'^transaction_create/$',views.transaction_create, name='transaction_create'),
   	url(r'^search_amount/$',views.search_amount, name='search_amount'),
    url(r'^search_card_type/$',views.search_card_type, name='search_card_type'),
   	url(r'^card/$',views.card, name='card'),
   	url(r'^card_add/$',views.card_add, name='card_add'),
   	url(r'^(?P<card_pk>[0-9]+)/card_delete/$',views.card_delete, name='card_delete'),
   	url(r'^client/$',views.client, name='client'),
   	url(r'^client_add/$',views.client_add, name='client_add'),
   	url(r'^(?P<client_pk>[0-9]+)/client_delete/$',views.client_delete, name='client_delete'),
   	url(r'^staff/$',views.staff, name='staff'),
   	url(r'^staff_add/$',views.staff_add, name='staff_add'),
   	url(r'^(?P<staff_pk>[0-9]+)/staff_delete/$',views.staff_delete, name='staff_delete'),

]