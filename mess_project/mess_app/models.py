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
    item = models.CharField(max_length=30)


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

class mess_menu(models.Model):
    day = models.CharField(max_length=10)
    items = models.TextField()
    menu_id = models.IntegerField()
class serves(models.Model):
    menu_id = models.IntegerField()
    mess_id = models.IntegerField()
    meal_type = models.TextField()
class guest(model.Model):
    guest_id = models.CharField(max_length=10)
    name = models.CharField('Guest Name',max_length=50)
    phone = models.CharField('Guest Contact',max_length=20)
class eats(mosels.Model):
    guest_id = models.CharField(max_length=10)
    payment = models.IntegerField()
    meal_type = models.TextField()
    mess_id = models.IntegerField()
class mess_council(models.Model):
    council_id = models.IntegerField()
    mess_id = models.IntegerField()
    head = models.CharField(max_length=20)
class member(models.Model):
    s_id =  models.IntegerField()
    member_id = models.CharField('Mess member_id',max_length=10)
    council_id = models.IntegerField()
    joining_date = models.DateTimeField()
class registers(models.Model):
    s_id =  models.IntegerField()
    mess_id = models.IntegerField()
    semester = models.CharField('Semester',max_length=10)
    payment = models.IntegerField()
    joining_date = models.DateTimeField()
class student(models.Model):
    s_id =  models.IntegerField()
    s_name =  models.CharField('Student_Name',max_length=50)
    email_id = EmailField(max_length = 254)
    phone = models.CharField('Student Contact',max_length=20)
class feedback(models.Model):
    feedback_id = models.IntegerField()
    s_id =  models.IntegerField()
    council_id = models.IntegerField()
    complaint = models.TextField()
    status = models.CharField(max_length=6)
    date = models.DateTimeField()
