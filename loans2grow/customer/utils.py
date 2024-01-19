from twilio.rest import Client
from django.conf import settings


def send_otp(mobile):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    verification = client.verify.v2.services(settings.TWILIO_VERIFIED_SID).verifications.create(
        to=mobile,
        channel="sms"
    )
    return verification.status


def check_otp(mobile,otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    verification_check = client.verify.v2.services(settings.TWILIO_VERIFIED_SID).verification_checks.create(
        to=mobile,
        code=otp
    )
    return verification_check.status