from django.core.mail import EmailMessage
from datetime import datetime
import base64
from django.core.mail import EmailMessage

class SendApplicationMail:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(subject=data.get('subject'), body=data.get('email_body'),to=[data.get('to customer')])
        email.send()

def send_loan_disbursement_email(to_email, amount, gst_amount, transaction_details):
    subject = 'Loan Disbursement Details'
    message = f'Your loan amount of {amount} has been successfully disbursed.\n'
    message += f'GST Amount: {gst_amount}\nTransaction Details: {transaction_details}'

    from_email = 'loansgrow@gmail.com'  
    email = EmailMessage(subject, message, from_email, [to_email])
    email.send()




def generate_transaction_details(amount, gst_amount, payment_mode, disbursed_to_account_no):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_details = (
        f"Transaction successful.\n"
        f"Amount: {amount}\n"
        f"GST Amount: {gst_amount}\n"
        f"Payment Mode: {payment_mode}\n"
        f"Disbursed to Account No: {disbursed_to_account_no}\n"
        f"Timestamp: {timestamp}"
    )
    return transaction_details