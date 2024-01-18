import base64
from django.core.mail import EmailMessage

def encode_application_id( app_id : str) -> str:
    app_bytes = app_id.encode('ascii')
    base64_bytes = base64.b64encode(app_bytes)
    base64_app_id = base64_bytes.decode('ascii')
    return base64_app_id

def decode_application_id(app_id:str) -> str:
    base64_bytes = base64.b64decode(app_id)
    return base64_bytes.decode('ascii')

class SendApplicationMail:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(subject=data.get('subject'), body=data.get('email_body'),to=[data.get('to customer')])
        email.send()






































# from django.core.mail import send_mail
# from django.http import HttpResponse


# def send_email_with_Application_id(request):
#     application_id = ''
#     customer_email = ''
#     subject = 'Application Submission Confirmation'
#     message = f'Thank you for submitting your application! Your application ID is: {application_id}'

#     from_email = ''  
#     recipient_list = [customer_email]
#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse('Email sent successfully!!')