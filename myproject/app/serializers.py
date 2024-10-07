from rest_framework import serializers
from .models import ImageUpload
from django.contrib.auth.models import User
class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['user', 'image']  # Include user in the fields

    def create(self, validated_data):
        # Associate the image upload with the authenticated user
        user = validated_data.pop('user')
        image_upload = ImageUpload.objects.create(user=user, **validated_data)
        return image_upload


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

