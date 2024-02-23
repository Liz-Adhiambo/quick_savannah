from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer,UserSerializer,LoginSerializer
import requests
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .africas import *
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        number=request.data.get('number')
        if serializer.is_valid():
            user=serializer.save()
            if number:
                Customer.objects.create(user=user, number=number, name=user.username)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_view(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:

            profile = Customer.objects.get(user=user)
            refresh = RefreshToken.for_user(user)
            serialized_data = {
                'user_id': profile.user.id,
                'user_name': profile.user.username,
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            return Response({'data':serialized_data})
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order=serializer.save()
 
            customer_number=order.customer.number
            print(customer_number)
            SMS().send(customer_number)
                

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def google_login(request):
    token = request.data.get('token')
    if token is None:
        return Response({'error': 'Google token not provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        google_info_url = f'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token}'
        google_response = requests.get(google_info_url)
        google_response.raise_for_status()
        google_data = google_response.json()
    except requests.exceptions.RequestException as e:
        return Response({'error': 'Failed to verify token'}, status=status.HTTP_400_BAD_REQUEST)

    email = google_data.get('email')
    google_id = google_data.get('sub')

    if email is None or google_id is None:
        return Response({'error': 'Failed to extract information from Google'}, status=status.HTTP_400_BAD_REQUEST)

    User = get_user_model()
    user, created = User.objects.get_or_create(email=email, defaults={'username': email, 'provider': 'google'})
    
    if created:
        user.set_unusable_password()
        user.save()

    refresh = RefreshToken.for_user(user)

    return Response({'message': 'User logged in successfully','token':refresh}, status=status.HTTP_200_OK)