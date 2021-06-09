from django.db import models
import uuid
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class Exchange(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(("created_at"), auto_now_add=True)