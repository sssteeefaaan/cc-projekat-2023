from django.db import models

# Create your models here.
class Professor(models.Model):
    firstName = models.CharField(max_length=20, null=False)
    lastName = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=20, null=False, unique=True, db_index=True)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    umcn = models.CharField(max_length=13, null=False, db_index=True, unique=True)
    idCardNumber = models.CharField(max_length=14,null=False, db_index=True, unique=True)
    phoneNumber = models.CharField(max_length=14, null=False, unique=True, db_index=True)
    address = models.ForeignKey('home.Address', on_delete=models.CASCADE, null=False)
    faculty = models.ManyToManyField('home.Faculty', blank=True, null=True)
    image = models.ImageField(upload_to="images/professors")


    def __str__(self) -> str:
        return f"{self.umcn} {self.lastName} {self.firstName}"