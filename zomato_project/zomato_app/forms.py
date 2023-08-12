# zomato_app/forms.py
from django import forms
from .models import Dish, Order

from .models import Feedback


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'dishes', 'status']

# customer feedback system
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['dish', 'rating', 'comment']
