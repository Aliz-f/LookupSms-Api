#!/usr/bin/env python
from kavenegar import *
import redis

kaveh_api = 'KaveNegar API'

def otp(phone_number, token):
    try:
        api = KavenegarAPI(kaveh_api)
        params = {
            'receptor': phone_number,
            'template': 'karimoo',
            'token': token,
            'type': 'sms',#sms vs call
        }
        cache = redis.StrictRedis()
        cache.set(str(phone_number), json.dumps({"token": token, "singup": False}))
        cache.expire(str(phone_number),time=120)   
        response = api.verify_lookup(params)
        print(response)
        return response, cache
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)