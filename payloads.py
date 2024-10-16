# from assistant_methods import generate_random_email, generate_random_string, generate_phone_number
import string
import random


def new_user_payload():
    payload = {
        "email": generate_random_email(),
        "first_name": generate_random_string(5),
        "phone_number": generate_phone_number(),
    }
    return payload


def new_card_payload():
    payload = {
        # "images": "",
        "title": "Test Card",
        # "description": "",
        "connect_method": "only_calls",
        "price": 1000,
        "new_or_used": "new",
        "category": 5,  # "Личные вещи"
        "city": 2       # Санкт-Петербург
    }
    return payload


def new_service_card_payload():
    payload = {
        # "images": "",
        "title": "Test Service Card",
        # "description": "",
        "connect_method": "only_calls",
        # "price": 1000,
        "price_type": "per_unit",
        "category": 5,
        "city": 2
    }
    return payload


def notification_payload(user_id):
    payload = {
        "title": "test notification",
        "description": "test notification",
        "users": [user_id]
    }
    return payload


def read_notification_payload():
    payload = {
        "is_read": True
    }
    return payload


def unread_notification_payload():
    payload = {
        "is_read": False
    }
    return payload


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_email():
    email = generate_random_string(5)
    email += '@test.com'
    return email


def generate_phone_number():
    phone_number = '89'  # чтобы номер был похож на настоящий
    for i in range(9):
        phone_number += random.choice(string.digits)
    return phone_number
