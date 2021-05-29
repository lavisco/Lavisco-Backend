from rest_framework import serializers
from .models import CustomUser

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']
        read_only_fields = ('email',)


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'