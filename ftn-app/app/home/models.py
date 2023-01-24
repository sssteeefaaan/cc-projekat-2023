from django.db import models

# Create your models here.

class Address(models.Model):
    postalCode = models.IntegerField()
    municipality = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.postalCode} {self.municipality} {self.name}"

class Faculty(models.Model):
    code = models.CharField(max_length=10, null=False, db_index=True, unique=True)
    name = models.CharField(max_length=50, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    phoneNumber = models.CharField(max_length=20, null=False, db_index=True, unique=True)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"
