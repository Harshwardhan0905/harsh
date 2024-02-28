from django.shortcuts import render
from django.http import HttpResponse
import razorpay
from .models import Apple
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
def home(request):
    if request.method == "POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_6WMPi1Me1Z2e8k","RM279RSAldAfsl5yQF0KL2ws"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        apple=Apple(name=name,amount=amount,payment_id=payment['id'])
        apple.save()
        return render(request,"index.html",{'payment':payment})
    return render(request,"index.html")

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        order_id=""
        for key,val in a.items():
            if key=="razorpay_order_id":
                order_id=val
                break
        user=Apple.objects.filter(payment_id=order_id).first()
        print(user)
    return render(request,"success.html")   