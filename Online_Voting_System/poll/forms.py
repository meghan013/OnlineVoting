from django import forms
from .models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    age = forms.IntegerField()  # Add the "age" field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not 18 <= age < 100:
            raise forms.ValidationError('You must be between 18 and below 100 to vote.')
        return age

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if username contains both letters and numerics
        if not any(char.isdigit() for char in username) or not any(char.isalpha() for char in username):
            raise ValidationError('Username must contain both letters and numerics.')
        # Check if username is unique
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')
        return username


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age','password']
        widgets = {
            'password': forms.PasswordInput,
        }



class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class VoterLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    voter_id = forms.IntegerField()
