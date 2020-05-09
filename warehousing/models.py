from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    telePhone = models.IntegerField()
    bank_account = models.IntegerField()

    def __str__(self):
        full_name = self.name + ' ' + self.last_name
        return full_name


class Entry(models.Model):
    seller = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    total_cost = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return '{} at {}'.format(self.seller, self.date)


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True

    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, blank=True)
    buy_cost = models.IntegerField()
    sell_cost = models.IntegerField(blank=True)
    profit = models.IntegerField(blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
    count = models.IntegerField()
    entries = models.ManyToManyField(
        Entry,
    )

    def __str__(self):
        return '{} x {}'.format(self.name, self.count)
