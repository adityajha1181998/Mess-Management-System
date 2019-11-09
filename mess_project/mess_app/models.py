from django.db import models

# Create your models here.


class mess(models.Model):
    mess_id = models.IntegerField()
    mess_name = models.CharField('Mess Name',max_length=50,blank=False)
    phone = models.CharField('Mess Contact',max_length=15)
    capacity = models.IntegerField()

# The above statement is equivalent to 
    # CREATE TABLE mess (
    #     mess_id int,
    #     mess_name varchar(50) not null,
    #     phone varchar(15),
    #     capacity int
    # )

class works(models.Model):
    staff_id = models.IntegerField()
    mess_id = models.IntegerField()

class staff(models.Model):
    staff_id = models.IntegerField()
    staff_name = models.CharField('Staff Name',max_length=50)
    designation = models.CharField('Post',max_length=45)
    salary = models.IntegerField()
    address = models.CharField(max_length=200,blank=False)
    phone = models.CharField(max_length=15)
    joining_date = models.DateTimeField()

class supplier(models.Model):
    sup_id = models.IntegerField()
    sup_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField('Mess Contact',max_length=15)

class inventory(models.Model):
    item_id = models.IntegerField()
    mess_id = models.IntegerField()
    quantity = models.IntegerField()

class consumption(models.Model):
    mess_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()

class purchase(models.Model):
    item_id = models.IntegerField()
    sup_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    price = models.IntegerField()
    bill_id = models.IntegerField()

class bills(models.Model):
    bill_id = models.IntegerField()
    date = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(max_length=6)
    bill_type = models.CharField(max_length=50)
    mess_id = models.IntegerField()

class expenses(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()