from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Student


class Questions(models.Model):
    CAT_CHOICES = (
    ('technical','Technical'),
    ('aptitude','aptitude'),

    )
    question = models.TextField(max_length = 300)
    optiona = models.TextField(max_length = 100)
    optionb = models.TextField(max_length = 100)
    optionc = models.TextField(max_length = 100)
    optiond = models.TextField(max_length = 100)
    answer = models.TextField(max_length = 100)
    category = models.CharField(max_length=20, choices = CAT_CHOICES,default='Technical')

    

    class Meta:
        ordering = ('-category',)

    def __str__(self):
        return self.question

    def get_types(self):
        return self.category


class Scores(models.Model):
    TotalMarks = models.CharField(max_length=100, )
    user = models.ForeignKey(Student, on_delete=models.CASCADE, default=True)

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return str(self.user)



