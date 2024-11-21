import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def trigger(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0769302489'
    amount = 1
    account_reference = '001-ABC'
    transaction_desc = 'x-services'
    callback_url = 'https://willingly-tolerant-clam.ngrok-free.app//callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

@csrf_exempt
def callback(request):
    resp = json.loads(request.body)
    print(resp)
    return HttpResponse("OK")




#chatsasa
#mobilesasa