from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.CharField(null=True, max_length=100)
    phone_number = models.CharField(null=True, max_length=100)
    rank = models.CharField(null=True, max_length=100)
    office_location = models.CharField(null=True, max_length=100)
    service_num = models.CharField(null=True, max_length=100)
    username = models.CharField(null=True, max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'