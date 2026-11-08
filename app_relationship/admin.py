from django.contrib import admin
from .models import Person, Passport, Publisher, Author, Book
 
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
