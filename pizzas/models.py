from django.db import models

class Pizza(models.Model):
  name = models.CharField(max_length=60)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Topping(models.Model):
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  name = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'toppings'

  def __str__(self):
    return f"{self.name[:50]}..."