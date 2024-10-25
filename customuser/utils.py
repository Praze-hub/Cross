from django.core.mail import send_mail


class Mails:
    def send_signup_email(email):
        subject = 'Welcome to Cross'
        message = 'Thank you for'
        sender_email = 'godspraiseokechukwu07@gmail.com'
        recipient_list = [email]
        
        send_mail(subject, message, sender_email, recipient_list)