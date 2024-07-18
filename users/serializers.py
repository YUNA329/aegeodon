from rest_framework import serializers
from users.models import User
from pets.models import Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_nickname', 'pet']
        
class RegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id', 'login_pw', 'user_nickname']

class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id', 'login_pw']
        