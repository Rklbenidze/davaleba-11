from django.db import models

# OneToOne
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="passport")
    number = models.CharField(max_length=20, unique=True)
    issued_date = models.DateField()

    def __str__(self):
        return f"{self.number} ({self.person})"

# ForeignKey
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# ManyToMany
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title
