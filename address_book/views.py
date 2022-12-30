from django.shortcuts import render, redirect
from django.contrib import messages
from address_book.forms import AddressForm
from address_book.models import Address

def home(request) :
    all_addresses = Address.objects.all
    context = {
        'all_addresses' : all_addresses,
    }
    return render(request, 'pages/home.html', context)

def add_address(request) :
    all_fields = Address._meta.fields
    context = {
        'all_fields' : all_fields,
    }
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Address Has Been Added!'))
            return redirect('home')
        else:
            messages.error(request, ('Seems like There was an Error...'))
            return render(request, 'address/add_address.html', context)
    else:
        return render(request, 'address/add_address.html', context)

def edit(request, list_id):
	if request.method == 'POST':
		current_address = Address.objects.get(pk=list_id)
		form = AddressForm(request.POST or None, instance=current_address)
		if form.is_valid():
			form.save()
			messages.success(request, ('Address Has Been Edited!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))
			return render(request, 'address/edit.html', {})	
	else:
		get_address = Address.objects.get(pk=list_id)
		return render(request, 'address/edit.html', {'get_address': get_address})

def delete(request, list_id):
	if request.method == 'POST':
		current_address = Address.objects.get(pk=list_id)
		current_address.delete()
		messages.success(request, ('Address Has Been Deleted...'))
		return redirect('home')
	else:
		messages.success(request, ('Nothing To See Here...'))
		return redirect('home')