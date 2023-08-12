
from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    dishes = models.ManyToManyField(Dish)
    status = models.CharField(
        max_length=50,
        choices=[
            ('received', 'Received'),
            ('preparing', 'Preparing'),
            ('ready', 'Ready for Pickup'),
            ('delivered', 'Delivered'),
        ],
        default='received'
    )

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'order_status_group',
                {
                    'type': 'update.status',
                    'status': f"Order {self.id} received"
                }
            )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


# Customer Feedback System
class Feedback(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.dish.dish_name} - Rating: {self.rating}"
