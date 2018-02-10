"""
We would like to see you come up with a solution that allows insurers to define their own custom data model for their risks.
 There should be no database tables called automobiles, houses, or prizes. 
Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.
Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. 
Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, 
number, currency, and so forth.

Data

For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. 
Field types should be either text, number, date, or enum (where there are multiple potential options but only one choice 
can be made).

Deliverables will be either...

A Python file containing the ORM classes for these tables.
An entity relationship diagram, which depicts the tables and their relationship to one another.
Both 1 and 2, because you're awesome.
"""

from django.db import models


class Insurer(models.Model):
    first_name = models.CharField(max_length=264)
    age = models.IntegerField()
    address = models.CharField(max_length=264, blank=True, null=True)
    zip_code = models.IntegerField()
    phone_no = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name


class RiskType(models.Model):
    insurer = models.ForeignKey(Insurer, on_delete=models.cascade)
    serial_number = models.IntegerField()
    risk_type_name = models.CharField(max_length=264)
    coverage_a_limit = models.IntegerField()
    prize_dollar_amount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.risk_type_name

