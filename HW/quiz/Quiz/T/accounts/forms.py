from django import forms
from . models import User ,OptCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1= forms.CharField(label='password' , widget=forms.PasswordInput)
    password2= forms.CharField(label='confirm password' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email' , 'phone_number' , 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match.')
        return cd['password2']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a herf=\" ../password/\" >this form </a>")
    class Meta:
        model = User
        fields = ('email' , 'phone_number' , 'full_name' , 'password' , 'last_login')


#_____________________________________________

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name=forms.CharField(label='full name' , max_length=20)
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(max_length=100 , widget=forms.PasswordInput)

    def clean_email(self):
        emial = self.cleaned_data['email']
        user= User.objects.filter(email=emial)
        if user:
            raise ValidationError('this email already exist...')
        return emial

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number)
        if user:
            raise ValidationError('this phone number already exist')
        OptCode.objects.filter(phone_number = phone_number).delete()
        return phone_number




class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()



class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20 , widget=forms.PasswordInput)


