from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to Wetiba subscription service \n"
            response += "1. Sport \n"
            response += "2. Politics \n"
            response += "3. Local \n"
            response += "4. International"

        elif text == "1":
            response = "CON Select Your Preferred Sport Plans \n"
            response += "1. Daily @ 15 \n"
            response += "2. Weekly @ 10 \n"
            response += "3. Monthly @ 5 "

        elif text == "1*1":
            response = "CON You will be charged KES 15 for your Daily Sports news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*1*1":
            response = "END Thank you for subscribing to our daily sport news plan \n"
        elif text == "1*1*2":
            response = "END Thank you for your one-off daily sport news plan \n"

        elif text == "1*2":
            response = "CON You will be charged KES 10 for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*2*1":
            response = "END Thank you for subscribing to our weekly sport news plan \n"
        elif text == "1*2*2":
            response = "END Thank you for your one-off weekly sport news plan \n"

        elif text == "1*3":
            response = "CON You will be charged KES 5 for our monthly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*3*1":
            response = "END Thank you for subscribing to our monthly sport news plan \n"
        elif text == "1*3*2":
            response = "END Thank you for your one-off monthly sport news plan \n"

        # Politics option handling
        elif text == "2":
            response = "CON Select Your Preferred Politics Plans \n"
            response += "1. Daily @ 20 \n"
            response += "2. Weekly @ 15 \n"
            response += "3. Monthly @ 10 "

        elif text == "2*1":
            response = "CON You will be charged KES 20 for your Daily Politics news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "2*1*1":
            response = "END Thank you for subscribing to our daily politics news plan \n"
        elif text == "2*1*2":
            response = "END Thank you for your one-off daily politics news plan \n"

        elif text == "2*2":
            response = "CON You will be charged KES 15 for our weekly Politics news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "2*2*1":
            response = "END Thank you for subscribing to our weekly politics news plan \n"
        elif text == "2*2*2":
            response = "END Thank you for your one-off weekly politics news plan \n"

        elif text == "2*3":
            response = "CON You will be charged KES 10 for our monthly Politics news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "2*3*1":
            response = "END Thank you for subscribing to our monthly politics news plan \n"
        elif text == "2*3*2":
            response = "END Thank you for your one-off monthly politics news plan \n"

        # Local news option handling
        elif text == "3":
            response = "CON Select Your Preferred Local News Plans \n"
            response += "1. Daily @ 10 \n"
            response += "2. Weekly @ 7 \n"
            response += "3. Monthly @ 5 "

        elif text == "3*1":
            response = "CON You will be charged KES 10 for your Daily Local news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "3*1*1":
            response = "END Thank you for subscribing to our daily local news plan \n"
        elif text == "3*1*2":
            response = "END Thank you for your one-off daily local news plan \n"

        elif text == "3*2":
            response = "CON You will be charged KES 7 for our weekly Local news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "3*2*1":
            response = "END Thank you for subscribing to our weekly local news plan \n"
        elif text == "3*2*2":
            response = "END Thank you for your one-off weekly local news plan \n"

        elif text == "3*3":
            response = "CON You will be charged KES 5 for our monthly Local news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "3*3*1":
            response = "END Thank you for subscribing to our monthly local news plan \n"
        elif text == "3*3*2":
            response = "END Thank you for your one-off monthly local news plan \n"

        # International news option handling
        elif text == "4":
            response = "CON Select Your Preferred International News Plans \n"
            response += "1. Daily @ 25 \n"
            response += "2. Weekly @ 20 \n"
            response += "3. Monthly @ 15 "

        elif text == "4*1":
            response = "CON You will be charged KES 25 for your Daily International news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "4*1*1":
            response = "END Thank you for subscribing to our daily international news plan \n"
        elif text == "4*1*2":
            response = "END Thank you for your one-off daily international news plan \n"

        elif text == "4*2":
            response = "CON You will be charged KES 20 for our weekly International news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "4*2*1":
            response = "END Thank you for subscribing to our weekly international news plan \n"
        elif text == "4*2*2":
            response = "END Thank you for your one-off weekly international news plan \n"

        elif text == "4*3":
            response = "CON You will be charged KES 15 for our monthly International news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "4*3*1":
            response = "END Thank you for subscribing to our monthly international news plan \n"
        elif text == "4*3*2":
            response = "END Thank you for your one-off monthly international news plan \n"

        return HttpResponse(response, content_type='text/plain')

    return HttpResponse("This endpoint is for USSD requests only.", content_type='text/plain')
