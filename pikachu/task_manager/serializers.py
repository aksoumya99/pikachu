from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['deadline', 'assigned_to', 'notes']


class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskForEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['time_estimated', 'notes', 'state']
