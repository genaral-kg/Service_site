from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    # def save(self, *args, **kwargs): Способ №1
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.name



@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


