from django import forms
from django.contrib.auth.models import User
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'date', 'description', 'color']

class UserRegisterForm(forms.ModelForm):  # Форма для регистрации пользователя
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']  # Поля для регистрации
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Хэшируем пароль
        if commit:
            user.save()
        return user