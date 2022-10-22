from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(default=0)

#гайд, по которому происходил полиморфизм: https://cpadiernos.github.io/how-to-add-fields-to-the-user-model-in-django.html