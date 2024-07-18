from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pets.models import Pet
from .serializers import PetSerializer
from users.models import User

@api_view(['POST'])
def pet_create(request):
    login_id = request.query_params.get('login_id')

    try:
        user = User.objects.get(login_id=login_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        pet = Pet.objects.create(
            user=user,
            pet_type=serializer.validated_data['pet_type'],
            pet_name=serializer.validated_data['pet_name'],
            pet_age=serializer.validated_data['pet_age']
        )

        response_data = {
            'login_id': login_id,
            'pet_id': pet.id,
            'pet_type': pet.pet_type,
            'pet_name': pet.pet_name,
            'pet_age': pet.pet_age
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pet_retrieve(request):
    login_id = request.query_params.get('login_id')

    try:
        user = User.objects.get(login_id=login_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    pets = Pet.objects.filter(user=user)
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

