from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Название товара',
    )
    description = models.CharField(
        max_length=300,
        verbose_name='Описание товара',
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='Цена'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name
