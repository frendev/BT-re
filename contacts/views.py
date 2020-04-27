from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.


def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
       
       #check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        #sending email 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()  
        FROM = "adwait1045@gmail.com"
        PASSWORD = 'Sergio_Ramos'

        #logging in
        server.login(FROM, PASSWORD)

        #template for recievers
        TOADDR = ["adwait.madhukar.gore@gmail.com",realtor_email]
        SUBJECT = "Property Inquiry"
        TEXT = "Hi, we have gotten your mail. Please Sign up on our site for further process. Thank You!"

        message = MIMEMultipart()
        message['From'] = "BT Real Estate <{}>".format(FROM)
        message['To'] = ', '.join(TOADDR)
        
        message['Subject'] = SUBJECT
        message.attach(MIMEText(TEXT))

        MSG = message.as_string()

        #Join reciever with CC
        FINAL_TO = TOADDR


        server.sendmail(FROM, FINAL_TO, MSG)


        messages.success(request,'Your request has been succesfully submitted! A realtor wil get back to you soon!')

        return redirect('/listings/'+listing_id)


