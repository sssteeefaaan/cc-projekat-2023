from django.db import models

class Parent(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20, unique=True, db_index=True, null=False)
    umcn = models.CharField(max_length=13, unique=True, db_index=True, null=False)
    idCardNumber = models.CharField(max_length=14, unique=True, db_index=True, null=False)
    address = models.ForeignKey('home.Address', on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f"{self.umcn} {self.lastName} {self.firstName}"


class Student(models.Model):
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    phoneNumber = models.CharField(max_length=20, unique=True, db_index=True, null=False)
    email = models.EmailField(unique=True, db_index=True, null=False)
    username = models.CharField(max_length=20, unique=True, db_index=True, null=False)
    password = models.CharField(max_length=50, null=False)
    umcn = models.CharField(max_length=13, unique=True, db_index=True, null=False)
    idCardNumber = models.CharField(max_length=14, unique=True, db_index=True, null=False)
    index = models.CharField(max_length=20, unique=True, db_index=True, null=False)
    faculty = models.ForeignKey('home.Faculty', on_delete=models.CASCADE, null=False)
    birthDate = models.DateField(null=False)
    address = models.ForeignKey('home.Address', on_delete=models.CASCADE, null=False)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to="images/students")

    def __str__(self) -> str:
        return f"{self.index} {self.lastName} {self.firstName}"
