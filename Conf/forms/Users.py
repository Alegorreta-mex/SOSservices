from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
