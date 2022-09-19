from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def password(request):
    Numbers = list('0123456789')
    Chars = list('abcdefghijklmnopqrstuvwxyz')
    UppercaseChars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    SpecialChars = list('!@#$%^&*(+-)')

    length_of_password = int(request.GET.get('length'))
    type_of_password = request.GET.get('type')

    password = ''

    if type_of_password == 'letters':
        for x in range(length_of_password):
            password += random.choice(Chars + UppercaseChars)
    if type_of_password == 'letters_and_numbers':
        for x in range(length_of_password):
            password += random.choice(Chars + UppercaseChars + Numbers)
    if type_of_password == 'all_characters':
        for x in range(length_of_password):
            password += random.choice(Numbers + Chars + UppercaseChars + SpecialChars)

    return render(request, 'password.html', {'password': password})