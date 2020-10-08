from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    Sterling = 'St'
    BharatiVidyapeeth = 'BVIT'
    SIES = 'si'
    ACPatil = 'Ac'
    YMT = 'YMT'
    others = 'others'

    college = (
        (Sterling, 'Sterling'),
        ( BharatiVidyapeeth, ' Bharati Vidyapeeth'),
        (SIES, 'SIES'),
        (YMT, 'YMT'),
        (others, 'others'),
    )
    college = models.CharField(max_length=20,
                                      choices=college,
                                      default=Sterling)


    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    mobile = models.CharField(max_length=20, null=False)
    roll_no = models.IntegerField(null=True)



    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name



# Create your models here.
