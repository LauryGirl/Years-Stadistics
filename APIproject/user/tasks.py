import random

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template


def send_mail(to, subject, message):
    subject = subject
    msg = EmailMessage(subject, message, to=to)
    msg.content_subtype = 'html'
    msg.send()


def is_admin(user):
    for role in user.roles.all():
        if role.admin:
            return True
    return False


def send_code(user, message, email):
    """
    Sends a verification code to a given User.\n
    The send method can be specified (email).\n
    """

    message = message

    if email:

        code = ''
        for char in message:
            if char >= '0' and char <= '9':
                code += char

        context = {
            'user_name': user.name,
            'code': code,
        }

        # message = get_template(
        #     'mailing/verification_code.html').render(context)
        
        message = Template("Code: {{code}}, User: {{user_name}}.")
        message.render(context)

        send_mail([user.email], "Recupera tu contraseña", message)

    return HttpResponse("Message sent")


def generate_code():
    return random.randint(1000, 9999)
