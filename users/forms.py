from django.forms import ModelForm, PasswordInput, CharField

from users.models import User


class RegisterForm(ModelForm):
    username = CharField(max_length=100, label="Login")
    password = CharField(widget=PasswordInput, label="Haslo")
    first_name = CharField(max_length=100, label="Imie")
    last_name = CharField(max_length=100, label='Nazwisko')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password")

