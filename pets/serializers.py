from rest_framework import serializers
from users.models import User
from pets.models import Pet

class PetRequsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['pet_type', 'pet_name', 'pet_age']

class PetSerializer(serializers.ModelSerializer):
    login_id = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ['login_id', 'id', 'pet_type', 'pet_name', 'pet_age']

    def get_login_id(self, obj):
        return obj.user.login_id if obj.user else None