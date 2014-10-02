from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_business_map(models.Model):
    business_clues=(
        (u'C',u'Garments'),
        (u'L',u'Lighting'),
        (u'D',u'Drinks'),
        (u'G',u'Groceries'),
        (u'A',u'Admin')
    )
    user=models.ForeignKey(User,to_field='id',primary_key=True)
    category=models.CharField(max_length=1,choices=business_clues)