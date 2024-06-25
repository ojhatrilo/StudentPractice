from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.http import HttpResponse
from django.contrib.sessions.models import Session

# Create
def create_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            item = Item(name=name)
            item.save()
            request.session['message'] = 'Item created successfully!'
            response = redirect('item_list')
            response.set_cookie('last_action', 'create')
            return response
    return render(request, 'create_item.html')

# Read
def item_list(request):
    items = Item.objects.all()
    message = request.session.get('message', '')
    last_action = request.COOKIES.get('last_action', '')
    return render(request, 'item_list.html', {'items': items, 'message': message, 'last_action': last_action})

# Update
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            item.name = name
            item.save()
            request.session['message'] = 'Item updated successfully!'
            response = redirect('item_list')
            response.set_cookie('last_action', 'update')
            return response
    return render(request, 'update_item.html', {'item': item})

# Delete
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.delete()
        request.session['message'] = 'Item deleted successfully!'
        response = redirect('item_list')
        response.set_cookie('last_action', 'delete')
        return response
    return render(request, 'delete_item.html', {'item': item})
