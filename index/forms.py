from django import forms
from index.models import *


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'用户名'}), max_length=30)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control login-field', 'placeholder':'密码'}), max_length=50)
    realname = forms.CharField(label='真实姓名', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'真实姓名'}), max_length=20)
    university = forms.CharField(label='学校名', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'学校名'}), max_length=20)

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'用户名'}), max_length=30)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control login-field', 'placeholder':'密码'}), max_length=50)

class PasswordForm(forms.Form):
    password = forms.CharField(label='原密码', widget=forms.PasswordInput(attrs={'class':'form-control login-field', 'placeholder':'原密码'}), max_length=50)
    newpwd = forms.CharField(label='新密码', widget=forms.PasswordInput(attrs={'class':'form-control login-field', 'placeholder':'新密码'}), max_length=50)
    repwd = forms.CharField(label='重复密码', widget=forms.PasswordInput(attrs={'class':'form-control login-field', 'placeholder':'重复密码'}), max_length=50)

class InvoiceForm(forms.Form):
    title = forms.CharField(label='发票抬头', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'发票抬头'}), max_length=50)
    invoicenum = forms.CharField(label='纳税人识别号', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'纳税人识别号'}), max_length=100)
    address = forms.CharField(label='快递地址', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'快递地址'}), max_length=100, required=False)
    postal = forms.CharField(label='邮政编码', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'邮政编码'}), max_length=100, required=False)
    phone = forms.CharField(label='手机号', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'手机号'}), max_length=100, required=False)
