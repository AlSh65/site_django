from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='slider/')
    css_slider = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
