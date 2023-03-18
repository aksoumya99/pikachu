from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task
from .serializers import PokemonSerializer, TaskSerializer, GetTaskSerializer, TaskForEmployeeSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import Count
from .constants import SUCCESS

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PokemonSerializer


class GeneralTaskView(APIView):

    def get(self, request):
        sort_by = request.query_params.get('sort_by', None)
        if sort_by is not None:
            tasks = Task.objects.order_by(sort_by)
        else:
            tasks = Task.objects.all()
        serializer = GetTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificTaskView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = GetTaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskForEmployeeView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskForEmployeeSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        tasks = Task.objects.filter(assigned_to_id=id)
        serializer = GetTaskSerializer(tasks, many=True)
        return Response(serializer.data)


class ProductivityView(APIView):

    def get(self, request):
        result = Task.objects.values('assigned_to').annotate(tasks_completed=Count('id'))
        print(result)
        return Response(result)
