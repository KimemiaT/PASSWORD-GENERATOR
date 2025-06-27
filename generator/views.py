from django.shortcuts import render
import string
import random

def home(request):
    return render(request, 'generator/home.html')

def generate_password(request):
    length = int(request.GET.get('length', 12))
    include_uppercase = request.GET.get('uppercase')
    include_numbers = request.GET.get('numbers')
    include_special = request.GET.get('special')

    characters = list(string.ascii_lowercase)

    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special:
        characters.extend(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': password})
