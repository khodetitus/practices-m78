
from django.shortcuts import render ,redirect

from django.views import View
from . forms import UserRegistrationForm,VerifyCodeForm , UserLoginForm
import random
from utils import send_otp_code
from . models import OptCode , User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login ,logout ,authenticate

# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    def get(self,request):
        form = self.form_class
        return render(request , 'accounts/register.html' , {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code= random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone_number'] , random_code)
            OptCode.objects.create(phone_number= form.cleaned_data['phone_number'] , code=random_code)
            request.session['user_registration_info'] = {
                'phone_number':form.cleaned_data['phone_number'] ,
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password']
            }
            messages.success(request,'you registerd successfully.' , 'success')
            return redirect('accounts:verify_code')
        return render(request,'accounts/register.html' , {'form':form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    def get(self,request):
        form = self.form_class
        return render(request,'accounts/verify.html' , {'form':form})
    def post(self,request):
        user_session = request.session['user_registration_info']
        code_instanse = OptCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instanse.code:
                User.objects.create_user(user_session['phone_number'] , user_session['email'] ,
                                    user_session['full_name'] , user_session['password'])
                code_instanse.delete()
                messages.success(request,'you successfully registered' ,'success')
                return redirect('home:home')
            else:
                messages.error(request,'code is wrong' ,'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')



class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out successfully' , 'success')
        return redirect('home:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name , {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,phone_number = cd['phone_number'] , password = cd['password'])
            if user is not None:
                login(request , user)
                messages.success(request,'you logged in successfully' ,'success')
                return redirect('home:home')
            messages.error(request,'phone number or password is wrong...' ,'danger')
        return render(request,self.template_name , {'form':form})








