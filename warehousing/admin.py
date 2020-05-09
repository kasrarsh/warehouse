from django.contrib import admin

from .models import Person, Entry, Category, Product, Count

admin.site.register(Person)
admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Count)



