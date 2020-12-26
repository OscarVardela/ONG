from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    if request.method=="POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + "mensaje enviado por:" + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['fundacionporvenir.ong@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,"contacto.html")

    return render(request,"index.html")


def galeria(request):
    return render(request,'galeria.html')

def contacto(request):

    return render(request,"contacto.html")


