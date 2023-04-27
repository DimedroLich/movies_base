from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.PositiveIntegerField(null=True)
    budget = models.PositiveIntegerField(default=40_000_000)
    slug = models.SlugField(default='',null=False)
    director = models.ForeignKey(to='Director',on_delete=models.PROTECT, null=True,blank=True)
    actors = models.ManyToManyField(to='Actor')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args,**kwargs)

    def get_url(self):
        return reverse('about',args=[self.slug])

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    def get_absolute_url(self):
        return reverse('about_director',args=[self.id])


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE,'Мужчина'),
        (FEMALE,'Женщина'),
    )
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1,choices=GENDERS,default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актёр {self.first_name} {self.second_name}"
        return f'Актриса {self.first_name} {self.second_name}'


    def get_absolute_url(self):
        return reverse('about_actor',args=[self.id])