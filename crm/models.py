from django.db import models



class Status(models.Model):
    status = models.CharField(max_length=100)

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    binding = models.ForeignKey(Order, on_delete=models.CASCADE)
