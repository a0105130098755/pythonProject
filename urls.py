from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('attractions/', views.attraction_list, name='attraction_list'),
    path('visits/add/', views.add_visit, name='add_visit'),
    # 로그아웃, 등록 등의 경로 추가...
]
