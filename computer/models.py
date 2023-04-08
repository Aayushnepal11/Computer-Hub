from django.db import models
from uuid import uuid4
import string, random


def random_code_gen():
    """
        Generating the random code.
        String literals only.
    """
    codes = list()
    code_data = ''
    for _ in range(1, 11):
        codes.append(random.choice(string.ascii_letters))
    for data in codes:
        code_data += data
    return code_data


class ComputerBarnd(models.Model):
    id = models.IntegerField(editable=False, primary_key=uuid4)
    brand_name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='products')

    class Meta:
        verbose_name_plural="Computer Brands"
    
    def __str__(self):
        return self.brand_name

class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=150)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    ram = models.IntegerField()
    brand = models.ForeignKey(ComputerBarnd, related_name="brands", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Computer Specifications"
    
    def __str__(self):
        return self.generation

class Computer(models.Model):
    computer_code = models.CharField(max_length=20, default=random_code_gen, editable=False)
    computer = models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE, related_name="computer")
    quantity = models.IntegerField()
    unit_rate = models.IntegerField()
    total_price = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.total_price =  self.quantity * self.unit_rate
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Total: Rs.{self.total_price}"

