from django import forms
from index.models import *


class JoinForm(forms.Form):
    pnum = forms.CharField(label='参会人数', widget=forms.TextInput(attrs={'class':'form-control login-field', 'placeholder':'参会人数'}))
    livable = forms.ChoiceField(label='住宿', widget=forms.Select(attrs={'class':'form-control login-field', 'placeholder':'住宿'}), choices=[('不住宿','不住宿'),('可合住','可合住'),('单独住','单独住')])
    indate = forms.DateField(label='入住时间', widget=forms.DateInput(attrs={'class':'form-control login-field', 'placeholder':'2000-10-21'}), required=False)
    outdate = forms.DateField(label='离开时间', widget=forms.DateInput(attrs={'class':'form-control login-field', 'placeholder':'2000-10-25'}), required=False)
    invoice = forms.BooleanField(label='是否开发票', required=False)
