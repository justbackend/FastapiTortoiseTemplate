from tortoise import fields
from tortoise.models import Model


class User(Model):
    username=fields.CharField(max_length=32)
    password=fields.CharField(max_length=255)



