
from django.contrib import admin
from .models import User

# Đăng ký model User vào admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')  # Cột hiển thị trong danh sách
    search_fields = ('username',)  # Cho phép tìm kiếm theo username
    list_filter = ('username',)  # Cho phép lọc theo username
    ordering = ('id',)  # Sắp xếp theo id

