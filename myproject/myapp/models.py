from django.db import models
from mongoengine import Document, fields

from mongoengine import Document, StringField, DecimalField, IntField

class Product(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    price = DecimalField(min_value=0)
    stock = IntField(min_value=0)

# Create your models here.
