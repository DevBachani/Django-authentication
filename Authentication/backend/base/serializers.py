from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        models = Note
        fields = ['id','description']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        models = User
        fields = ['username']

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = User
        fields =['username','email','password']

    password = serializers.CharField(write_only=True)


    def create(self,Validated_data):
        user = User(
            username = Validated_data['username'],
            email = Validated_data['email']

        )
        user.set_password(Validated_data['password'])
        user.save()
        return user
