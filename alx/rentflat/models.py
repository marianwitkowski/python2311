from django.db import models

# Create your models here.
class Flat(models.Model):
    code = models.CharField(max_length=20, unique=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=200)
    rooms = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    price_m2 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    area = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} - {self.title} - {self.price}"

    class Meta:
        verbose_name = "Mieszkanie"
        verbose_name_plural = "Mieszkania"


class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agenci"