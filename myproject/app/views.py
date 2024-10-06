from django.shortcuts import render

#Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ImageUpload
from .serializers import ImageUploadSerializer,RegisterUserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def ImageUploadView(request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserRegister(request):
      serializer=RegisterUserSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def UserLogin(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
#         return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def UserLogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Log the user in
        login(request, user)

        # Get the session ID
        session_id = request.session.session_key
        
        # Ensure the session is saved and the session ID is set
        if session_id is None:
            request.session.save()  # This will create a session if not already created
            session_id = request.session.session_key

        # Optionally, print the session ID to the console (for debugging)
        print("Session ID:", session_id)
        
        # Return session ID along with the response
        return Response({'message': 'Login successful', 'session_id': session_id}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def custom_logout_view(request):
    logout(request)
    return Response({'message': 'User logged out successfully'})