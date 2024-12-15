
import importlib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ambassador, Inventory

# Create your views here.

def home(request):
    ambIdV = ''
    ambNameV = ''
    ambPosV = ''
    ambPnumberV = ''
    ambEmailV = ''
    ambSocialV = ''
    ambDateOfHireV = ''
    ambBirthdateV = ''
    ambAdrV = ''

    itemIdV = ''
    itemNameV = ''
    itemQtyV = ''
    itemPriceV = ''
    itemDescV = ''
    if request.method == 'POST':
        ambIdV = request.POST['ambIdV']
        ambNameV = request.POST['ambNameV']
        ambPosV = request.POST['ambPosV']
        ambPnumberV = request.POST['ambPnumberV']
        ambEmailV = request.POST['ambEmailV']
        ambSocialV = request.POST['ambSocialV']
        ambDateOfHireV = request.POST['ambDateOfHireV']
        ambBirthdateV = request.POST['ambBirthdateV']
        ambAdrV = request.POST['ambAdrV']
        ambV = Ambassador(ambIdV, ambNameV, ambPosV, ambPnumberV, ambEmailV, ambSocialV, ambDateOfHireV, ambBirthdateV, ambAdrV)
        ambV.save()

        itemIdV = request.POST['itemIdV']
        itemNameV = request.POST['itemNameV']
        itemQtyV = request.POST['itemQtyV']
        itemPriceV = request.POST['itemPriceV']
        itemDescV = request.POST['itemDescV']
        inventoryV = Inventory(itemIdV, itemNameV, itemQtyV, itemPriceV, itemDescV)
        inventoryV.save()

    ambV = Ambassador.objects.all()
    inventoryV = Inventory.objects.all()
    return render(request, 'nsApp/index.html', {'data': ambV, 'data2': inventoryV})

# def home(request):
#     ambV = Ambassador.objects.all()
#     return render(request, 'nsApp/index.html', {'data': ambV})

