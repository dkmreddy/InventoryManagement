from django.db import models
from django.contrib.auth.models import User
# Create your models here.
business_clues=(
        (u'C',u'Garments'),
        (u'L',u'Lighting'),
        (u'D',u'Drinks'),
        (u'G',u'Groceries'),
        (u'A',u'Admin')
    )
class user_business_map(models.Model):
    user=models.ForeignKey(User,to_field='id',primary_key=True)
    category=models.CharField(max_length=1,choices=business_clues)
    is_staff=models.BooleanField()
    password=models.CharField(max_length=50)
    
class exec_log(models.Model):
    user=models.ForeignKey(User,to_field='id')
    action=models.CharField(max_length=20)
    detail=models.CharField(max_length=100)
    section=models.CharField(max_length=1,choices=business_clues)    