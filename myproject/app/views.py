from django.shortcuts import render

#Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import ImageUpload
from .serializers import ImageUploadSerializer,RegisterUserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.middleware.csrf import get_token

@api_view(['POST'])
def ImageUploadView(request):
    if request.user.is_authenticated:
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def UserRegister(request):
      serializer=RegisterUserSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserLogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)



    
@api_view(['POST'])
def custom_logout_view(request):
    request.session.flush()
    logout(request)
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
#@csrf_exempt
def csrf_token_view(request):
    csrf_token = get_token(request)
    csrf_token_from_cookie = request.COOKIES.get('csrftoken')  # Generate the CSRF token
    print(csrf_token)
    return JsonResponse(csrf_token_from_cookie,safe=False)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Ensure user is logged in
# def get_user_images(request):
#     user = request.user
#     images = ImageUpload.objects.filter(user=user)  # Fetch images for the current user
#     serializer = ImageUploadSerializer(images, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)



