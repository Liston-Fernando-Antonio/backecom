from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', "email", "password")

        extra_kwargs = {
            'first_name': { 'required': True, "allow_blank": False },
            'last_name': { 'required': True, "allow_blank": False },
            'email': { 'required': True, "allow_blank": False },
            'password': { 'required': True, "allow_blank": False, 'min_length': 6 },
        }

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
       model = User
       fields = ('first_name', 'last_name', "email", "username", 'is_staff', 'is_superuser', 'role')

    def get_role(self, obj):
        profile = getattr(obj, 'profile', None)
        return profile.role if profile else 'customer'