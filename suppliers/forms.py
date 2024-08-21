from .models import *
from django import forms


class CreateSupplierForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Supplier
        fields = "__all__"
        widgets = {

            'supplier_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Supplier name'}
            ),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier phone'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact name'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier name'}),
        }
