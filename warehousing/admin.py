from django.contrib import admin

from .models import Person, Entry, Category, Product

admin.site.register(Person)
admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Product)



