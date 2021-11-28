from random import randint
from django.shortcuts import redirect, render
import redis
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .utils import otp

# Create your views here.


class getNumber(APIView):
    def post(self, request):
        data = request.data
        phone_number = data.get('phone_number', 'None')
        token = randint(1000, 9999)
        response, cache = otp(phone_number, token)
        if response and cache:
            return(redirect('/sms/check_number/'))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class checkToken(APIView):
    def post(self, request):
        data = request.data
        phone_number = data.get('phone_number', 'None')
        token = data.get('token', 'None')
        cache = redis.StrictRedis()
        if cache.exists(str(phone_number)):
            cache_data = cache.get(str(phone_number))
            cache_data = json.loads(cache_data)
            cache_token = str(cache_data.get('token'))
            cache_isRegister = cache_data.get('singup')
            
            if cache_isRegister == False:
                if token == cache_token:
                    verify = redis.StrictRedis()
                    verify.set(str(phone_number), json.dumps({'verified': True}))
                    return(redirect('/sms/register/'))
                else:
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return(redirect('/sms/singin/'))
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class singin(APIView):
    pass

class register(APIView):
    pass