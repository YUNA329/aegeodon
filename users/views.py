from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from users.serializers import RegisterRequestSerializer, LoginRequestSerializer
from pets.serializers import PetSerializer
from pets.models import Pet

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = RegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)  # created를 _로 무시
            return Response({
                'user_id': user.id,
                'login_id': user.login_id,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            login_id = serializer.validated_data['login_id']
            login_pw = serializer.validated_data['login_pw']
            
            try:
                user = get_user_model().objects.get(login_id=login_id)
                if user.check_password(login_pw):
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({
                        'user_id': user.id,
                        'login_id': user.login_id,
                        'token': token.key
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except get_user_model().DoesNotExist:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def user_detail(request):
    if request.method == 'GET':
        login_id = request.query_params.get('login_id')
        if login_id:
            try:
                user = get_user_model().objects.get(login_id=login_id)
                pet = Pet.objects.get(user=user)
                pet_serializer = PetSerializer(pet)
                
                return Response({
                    'user_id': user.id,
                    'user_nickname': user.nickname,
                    'pet_id': pet.id,
                    'pet_type': pet_serializer.data['type'],
                    'pet_name': pet_serializer.data['name'],
                    'pet_age': pet_serializer.data['age']
                }, status=status.HTTP_200_OK)
            except get_user_model().DoesNotExist:
                return Response({'error': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except Pet.DoesNotExist:
                return Response({'error': 'Pet Not Found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Login ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)