from django.conf import settings
from django.db import models
from solo.models import SingletonModel

class Config(SingletonModel):
    # parameter to determine how long a verification code will remain available to be verified(in minutes).
    verification_code_validation_time = models.IntegerField(default=30)

    # parameters for recover password process

    # parameter to determine how long a token for recover password will remain valid (in days)
    recover_password_token_validation_time = models.IntegerField(default=1)
    recover_password_url = models.CharField(
        max_length=1024, blank=True, null=True)
    recover_password_contact_us_url = models.CharField(
        max_length=1024, blank=True, null=True)


    def __str__(self):
        return 'Config Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Config, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj