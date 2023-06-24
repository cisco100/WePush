from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import views as reset_view
from django.shortcuts import render, redirect
from certify.forms import SignInForm,SignUpForm
from django.urls import reverse_lazy

def login_view(request):
    form=SignInForm(request.POST or None)
    msg=None
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                #return redirect(reverse_lazy("home"))
            else:
                msg="Invalid Credntials"
                form=SignInForm()
        else:
            msg="Validation Error"

    return render(request,'auth/login.html',{"form":form,"msg":msg})









def register_view(request):
    msg=None
    success=True
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            true_password=form.cleaned_data.get("password1")
            #print(username,true_password)
            user=authenticate(username=username,password=true_password)
            #msg = 'User created - please <a href="/auth/login">login</a>.'
            success = True
            return redirect(reverse_lazy("login"))
        else:
            msg="Error registering user"
    else:
        form=SignUpForm()

    return render(request,"auth/register.html",{"form":form,"msg":msg,"success":success})





def logout_view(request):
    logout(request)
    bye_msg='Thanks for using ---! See Yah!<a style="color:red; "href="{% url login%}"> Login Again</a>'
    return render(request,"auth/logout.html",{'msg':bye_msg})






class CustomPasswordResetView(reset_view.PasswordResetView):
    template_name = 'auth/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(reset_view.PasswordResetDoneView):
    template_name = 'auth/password_reset_done.html'

class CustomPasswordResetConfirmView(reset_view.PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(reset_view.PasswordResetCompleteView):
    template_name = 'auth/password_reset_complete.html'
    #success_url = reverse_lazy('login')
