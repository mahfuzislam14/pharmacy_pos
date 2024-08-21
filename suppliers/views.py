from django.shortcuts import render, redirect
from .forms import *
from .models import *


def suppliers_list(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'suppliers/suppliers.html', context)


def createSupplier(request):
    if request.method == 'POST':
        form = CreateSupplierForm(request.POST)

        if form.is_valid():
            manufactural = form.cleaned_data["is_manufactural"]
            name = form.cleaned_data["supplier_name"]
            phone = form.cleaned_data["supplier_phone"]
            contact_name = form.cleaned_data["contact_name"]
            contact_phone = form.cleaned_data["contact_phone"]
            Supplier(is_manufactural=manufactural, supplier_name=name, supplier_phone=phone,
                     contact_name=contact_name, contact_phone=contact_phone).save()
            return redirect('suppliers_list')

    else:
        form = CreateSupplierForm(auto_id=True, label_suffix=' ')
        form.order_fields(
            field_order=['supplier_name', 'supplier_phone', 'contact_name', 'contact_phone', 'is_manufactural'])
        context = {
            'supplier_form': form
        }
        return render(request, 'suppliers/create_supplier.html', context)


def updateSupplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if request.method == 'POST':
        form = CreateSupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('suppliers_list')
    else:
        form = CreateSupplierForm(
            auto_id=True, label_suffix=' ', instance=supplier)
        form.order_fields(
            field_order=['supplier_name', 'supplier_phone', 'contact_name', 'contact_phone', 'is_manufactural'])
        context = {
            'supplier_form': form
        }
        return render(request, 'suppliers/update_supplier.html', context)


def deleteSupplier(request, supplier_id):
    Supplier.objects.get(id=supplier_id).delete()
    return redirect('suppliers_list')
