from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth import views

from certify.models import Account,Captcha
from certify.forms import RegistrationForm


from rest_framework import mixins,generics

from certify.serializers import CaptchaSerializer



class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        #Querry the user entry with the captcha model

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['email', 'name', 'phone', 'date_of_birth', 'gender','picture', 'password','education_level','field_of_interest','update_me_on_my_field']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user


# class CustomLoginView(views.LoginView):
#     template_name = 'certi/login.html'
   



class CustomLogoutView(views.LogoutView):
    template_name = 'registration/logout.html'
   
   



class CaptchaView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=CaptchaSerializer
    queryset=Captcha.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class CaptchaViewDetailed(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CaptchaSerializer
    queryset=Captcha.objects.all()
    lookup_field="id"
    def get(self,request,id):
        return self.retrieve(request,id)

    def put(self,request,id):
        return self.create(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)







