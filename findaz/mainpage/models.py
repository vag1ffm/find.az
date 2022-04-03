from django.db import models

class Items(models.Model):
    item_name = models.CharField("Название или краткое описание товара", max_length=50)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

