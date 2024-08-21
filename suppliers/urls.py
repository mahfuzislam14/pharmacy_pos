from django.urls import path
from . import views

urlpatterns = [
    path('', views.suppliers_list, name='suppliers_list'),
    path('create/', views.createSupplier, name="create_supplier"),
    path('delete/<int:supplier_id>', views.deleteSupplier, name='delete_supplier'),
    path('update/<int:supplier_id>', views.updateSupplier, name="update_supplier"),
]
