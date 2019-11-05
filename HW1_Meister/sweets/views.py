from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from sweets.models import Sweet
from sweets.serializers import SweetSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def sweet_list(request):
    if request.method == 'GET':
        sweets = Sweet.objects.all()
        serializer = SweetSerializer(sweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def sweet_detail(request, pk):
    try:
        sweet = Sweet.objects.get(pk=pk)
    except Sweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SweetSerializer(sweet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SweetSerializer(sweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

