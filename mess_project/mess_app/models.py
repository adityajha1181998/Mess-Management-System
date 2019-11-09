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