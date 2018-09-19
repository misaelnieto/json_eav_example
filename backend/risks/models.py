from enum import Enum

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField, ArrayField, JSONField
from django.db import models


class Insurer(models.Model):
    """
    An entity which provides insurance a.k.a insurance company, insurance
    carrier or underwriter.
    A person or entity who buys insurance is known as an insured or as a
    policyholder.
    """
    name = models.CharField(max_length=256)


class InsuranceSchema(models.Model):
    """
    We use the schema to compose the insurance and validate data input
    """
    title = models.CharField(max_length=256)
    description = models.TextField()
    insurer = models.ForeignKey(Insurer, on_delete=models.PROTECT)


class InsuranceField(models.Model):
    """
    This is one field in the insurance form when Insurer is editing it.
    """
    TEXT = 1
    NUMBER = 2
    DATE = 3
    ENUM = 4
    BOOLEAN = 5

    FIELD_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
        (ENUM, 'Choice'),
        (BOOLEAN, 'Boolean'),
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    data_type = models.IntegerField(choices=FIELD_TYPE_CHOICES)
    choices = ArrayField(
        models.CharField(max_length=256),
        default=list
    )
    schema = models.ForeignKey(
        InsuranceSchema,
        on_delete=models.PROTECT,
        related_name='fields'
    )


class InsuranceRecord(models.Model):
    """
    This is an actual record of the insurance. Data validated by InsuranceSchema
    is contained in the data field as Postgres' JSON field (jsonb).
    """
    schema = models.ForeignKey(InsuranceSchema, on_delete=models.PROTECT)
    insurer = models.ForeignKey(Insurer, on_delete=models.PROTECT)
    data = JSONField()

