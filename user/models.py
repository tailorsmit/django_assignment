from django.db import models
from django.contrib.auth import get_user_model


class Otp(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.otp
