from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Review(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    review_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.comment}"

    def get_absolute_url(self):
        return reverse('product_detail', args=(str(self.product_id)))
