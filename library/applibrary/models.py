
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    age_from =models.IntegerField()
    age_until =models.IntegerField()
    lending_time=models.IntegerField()
    def __str__(self):
        return f'{self.category_name} age: {self.age_from} - {self.age_until} ,lending_time: {self.lending_time}'

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    is_lend = models.BooleanField()
    image = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_name} category: {self.category}, is_lend: {self.is_lend} '


class Barrowed_book(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_barrowed = models.DateField()
    date_required_return = models.DateField()