from django.contrib.auth import get_user_model
from django.db import models

from category.models import Category

User = get_user_model()

# class PostImages(models.Model):
#    title = models.CharField(max_length=150, blank=True)
#    image = models.ImageField(upload_to='images/')
#    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
#
#    @staticmethod
#    def generate_name():
#       from random import randint
#       return 'image' + str(randint(100000, 1000000))
#
#    def save(self, *args, **kwargs):
#       self.title = self.generate_name()
#       return super(PostImages, self).save(*args, **kwargs)


class Uslugi(models.Model):
    owner = models.ForeignKey(User,related_name='uslugi',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    experience = models.PositiveSmallIntegerField(blank=True,null=True)
    working_days = models.CharField(max_length=200,blank=True,null=True)
    hour_from = models.PositiveSmallIntegerField(blank=True,null=True)
    hour_to = models.PositiveSmallIntegerField(blank=True,null=True)
    desc = models.CharField(max_length=250, null=True, blank=True)
    price = models.PositiveSmallIntegerField(blank=True,null=True)
    image2 = models.ImageField(upload_to='media/uslugi/',blank=True,null=True)



    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.title} -> {self.owner}'





