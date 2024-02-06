from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Customer


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        # exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        if not self.instance.user.is_staff:  # Assuming admin users have 'is_staff' set to True
            self.fields['user'].disabled = True

