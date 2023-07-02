from django.urls import path
from django.contrib.auth import views as auth_views

from certify import views


urlpatterns = [

    path('register/', views.RegistrationView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('captcha',views.CaptchaView.as_view()),
    path('captcha-detailed/<str:id>/',views.CaptchaViewDetailed.as_view())
]
