
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import *
     
def index(request):
	if request.method == 'POST':
		form = events_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/events/')
	else:
		form = events_form()

	return render(request, 'events/index.html', {'form' : form})			
	
def detail(request):
    
    name = request.POST.get('name')
    roll_no = request.POST.get('roll_no')

    products = Product.objects.all()
    total_count = Product.objects.all().count()
    for p in products:
        id = p.product_id
        q = request.POST.get('q_id_' + str(id))
        if q is not None and q != '' and int(q):
            q = int(q)
            amount += q * int(p.product_price)
            count += 1

    context = {
        'count': count,
        'amount': amount
    }
    return render(request, "events/detail.html", context)