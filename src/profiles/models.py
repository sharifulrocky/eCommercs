from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='Default description')

    def __str__(self):
        return self.name
