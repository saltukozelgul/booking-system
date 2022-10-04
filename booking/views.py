from django.shortcuts import redirect, render
from django.contrib import messages
from pymongo import MongoClient
from booking.forms import ReservationForm
import booking.db_utils as mongo
from django.http import HttpResponse, JsonResponse



client = MongoClient("your-url")
# Create your views here.
def main(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "main.html")

def choose(request):
    count1 = list(mongo.getUsersFromMongo(client, "1"))
    count2 = list(mongo.getUsersFromMongo(client, "2"))
    context = {"count1": count1, "count2": count2}
    return render(request, "reservation.html", context)

def reservation(request, id):
    users = list(mongo.getUsersFromMongo(client,id))
    if request.method == "POST":
        data = ReservationForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data)
            data.cleaned_data["activity_id"] = id
            msg = mongo.addReservationToMongo(client, data.cleaned_data)
            clearMessages(request)
            sendMessage(request, msg)
            return redirect('reservation', id=id)
        else:
            clearMessages(request)
            sendMessage(request, "Rezervasyon işleminiz gerçekleştirilemedi.{E}")
            sendMessage(request, "Lütfen bilgileri doğru girdiğinizden emin olun.{E}")
    context = {"id": id, "users": users}
    return render(request, "activity.html", context)

def delete(request):
    if request.method == 'POST':
        #getting page number
        number = request.POST.get('number', None) 
        id = request.POST.get('id', None) 
        print(f"number:{number},id:{id}")
        founded = mongo.getReservationByIdAndNumber(client, id, number)
        if founded:
            mongo.deleteReservationByIdAndNumber(client, id, number)
            return JsonResponse({"status":"deleted"})
        return JsonResponse({"status":"not found"})
    return redirect(request, 'reservation')
    #mongo.deleteReservation(client)


def clearMessages(request):
    storage = messages.get_messages(request)
    storage.used = True

def sendMessage(request,msg):
    clearMessages(request)
    if ("{E}" in msg):
        messages.error(request, msg.replace("{E}", ""))
    elif ("{S}" in msg):
        messages.success(request, msg.replace("{S}", ""))
    else:
        messages.info(request, msg)