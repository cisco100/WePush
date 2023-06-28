
from django.urls import path
from certify import views



urlpatterns = [
    path("login/",views.login_view,name="login"),
    path("register/",views.register_view,name="register"),
    path("logout/",views.logout_view,name="logout"),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('captcha',views.CaptchaView.as_view()),
    path('captcha-detailed/<str:id>/',views.CaptchaViewDetailed.as_view())
]