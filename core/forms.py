from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    # username = forms.CharField(
    #     max_length=150,
    #     required=True,
    #     help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы.',
    #     widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'})
    # )
    # email = forms.EmailField(required=True, help_text='Введите действительный адрес электронной почты.')

