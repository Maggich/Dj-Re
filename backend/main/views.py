from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product
from .models import Task
from .serializers import TaskSerializer


PRODUCTS = [
    {"id": 1, "title": "Ноутбук", "price": 300000, "in_stock": True},
    {"id": 2, "title": "Мышка", "price": 7000, "in_stock": False},
]


# class ProductListAPIView(APIView):
#     def get(self, request):
#         serializer = ProductSerializer(PRODUCTS, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskListCreateAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)