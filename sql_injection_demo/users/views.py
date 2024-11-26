from django.shortcuts import render
from django.db import connection

# Create your views here.
# users/views.py


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            query = f"SELECT * FROM users_user WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
        if user:
            return render(request, 'users/success.html')
        else:
            return render(request, 'users/fail.html')
    return render(request, 'users/login.html')