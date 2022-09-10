from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id':"form3Example4",'class':"form-control form-control-lg",'placeholder':"Введите логин"}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type':"password",'id':"form3Example4",'class':"form-control form-control-lg",'placeholder':"Введите пароль"}))