from django.contrib.auth import views, logout
from django.urls import path
from django.contrib import admin
from .views import registration, registration1
from . import views as local_view

urlpatterns = [

    path('login/', local_view.user_login,  name='login'),
    path('phone/', local_view.add_phone,  name='add_phone'),
    path('logout/', local_view.logout_view, name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', registration, name='register'),
    path('registration1', registration1, name='registration1')

]