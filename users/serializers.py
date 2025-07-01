from rest_framework import serializers
from .models import User, Role, Menu, Permission, MenuRole
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'code', 'description']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'path']


class MenuRoleSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = MenuRole
        fields = ['id', 'menu', 'permissions']


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
