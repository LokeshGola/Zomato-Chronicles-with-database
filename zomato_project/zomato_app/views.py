
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Order, Feedback
from .forms import DishForm, OrderForm, FeedbackForm


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})


# Display Menu and Orders
def menu(request):
    dishes = Dish.objects.all()  # Fetch all dishes from the database
    return render(request, 'menu.html', {'dishes': dishes})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


# Update Dish Availability and Order Status
def update_dish_availability(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        dish.available = not dish.available
        dish.save()
        return redirect('menu')
    return render(request, 'update_dish_availability.html', {'dish': dish})

def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order_status.html', {'form': form})

# chatbot function;
def chatbot(request):
    return render(request, 'chatbot.html')

# update dish details
def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    feedbacks = Feedback.objects.filter(dish=dish)
    form = FeedbackForm(request.POST or None, initial={'dish': dish})
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dish_detail', dish_id=dish_id)
    return render(request, 'dish_detail.html', {'dish': dish, 'feedbacks': feedbacks, 'form': form})

