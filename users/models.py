from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "siakad_role"

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)

    class Meta:
        db_table = "siakad_menu"

    def __str__(self):
        return self.name

class Permission(models.Model):
    code = models.CharField(max_length=100)  # view, add, edit, delete
    description = models.TextField()

    class Meta:
        db_table = "siakad_permission"

class MenuRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        db_table = "siakad_menu_role"

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "siakad_user"
