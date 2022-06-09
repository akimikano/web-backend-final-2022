from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from applications.shop.models import Order


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class OrderForm(ModelForm):
    user = forms.IntegerField(required=False)
    item = forms.IntegerField(required=False)

    class Meta:
        model = Order
        fields = ('user', 'item', 'address', 'promocode', 'size', 'color', 'phone')

    def save(self, commit=True):
        color = self.cleaned_data['color']
        size = self.cleaned_data['size']
        promocode = self.cleaned_data['promocode']
        phone = self.cleaned_data['phone']
        address = self.cleaned_data['address']
        user = self.initial['user']
        item = self.initial['item']
        order = Order.objects.create(user=user, item=item, color=color, size=size, address=address,
                                     phone=phone, promocode=promocode)
        return order

