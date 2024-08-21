from django.db import models

# Create your models here.


class Supplier(models.Model):
    is_manufactural = models.BooleanField()
    supplier_name = models.CharField(max_length=50)
    supplier_phone = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return super().__str__()
