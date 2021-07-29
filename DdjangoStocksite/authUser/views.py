from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serialIzers import AddressesSerializer, UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_name = data['name']
        obj = Addresses.objects.get(name=search_name)

        if data['phone_number'] == obj.phone_number:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Addresses.objects.all()
    post_list = AddressesSerializer('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")



@api_view(['POST'])
def signup(request):

  password = request.data.get('password')
  password_confirmation = request.data.get('passwordConfirmation')

  if password != password_confirmation:
    return Response({'error' : '비밀번호가 일치않습니다'},status=status.HTTP_400_BAD_REQUEST)


  serializer = UserSerializer(data=request.data)


  if serializer.is_vaild(raise_exception=True):
    user = serializer.save()

    user.set_password(request.data.get('password'))
    user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


