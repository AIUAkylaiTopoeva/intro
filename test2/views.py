from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . import serializers

@api_view(['GET'])
def get_sapros(request):
    vse_ludi = Person.objects.all()
    serialazer = serializers.PersonSerialazer(vse_ludi, many=True)
    return Response(serialazer.data, status=200)

@api_view(['GET'])
def get_sap(request, pk):
    try:
        chelovek = Person.objects.get(id = pk)
        serializer = serializers.PersonSerialazer(chelovek)
        print(serializer)
        return Response(serializer.data, status=200)
    except Person.DoesNotExist:
        return Response(f'Chelovek with id {pk} does not exist', status=404)

@api_view(['POST'])
def post_chela(request):
    serializer = serializers.PersonSerialazer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201 )

@api_view(['PUT', 'PATCH'])
def izmena(request, pk):
    try:
        chel = Person.objects.get(id=pk)
        if request.method =='PUT':
            serializer = serializers.PersonSerialazer(instance=chel, data = request.data)
        else:
            serializer = serializers.PersonSerialazer(instance=chel, data = request.data, partial = True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=206)
    except Person.DoesNotExist:
        return Response(f'Takogo cheloveka( c id {pk}) u vas net', status=404)

@api_view(['DELETE'])
def delete_chel(request, pk):
    try:
        chel = Person.objects.get(id = pk)
        chel.delete()
    except Person.DoesNotExist:
        return Response(f'Takogo cheloveka( c id {pk}) u vas net', status=404)