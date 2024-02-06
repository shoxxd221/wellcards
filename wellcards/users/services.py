import jwt

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed

from .tokens import account_activation_token
from .models import User
from wellcards.settings.base import SECRET_KEY


def edit_object(obj: object, **kwargs) -> None:
    """"Function that change values of object fields"""
    for key, value in kwargs.items():
        setattr(obj, key, value)
    obj.save()


def send_confirm_message_to_email(user: object, domain: str, form: object) -> None:
    """"Function that send confirm email to user email to finish the registration"""
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    EmailMessage('Activate your account.', message, to=[form.cleaned_data.get('username')]).send()


def get_user(request) -> object:
    """"Function that get user by JWT token"""
    token = request.META.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except:
        raise AuthenticationFailed('Unauthenticated')

    return User.objects.get(id=payload['user_id'])
