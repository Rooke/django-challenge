from django.db import models

class Home(models.Model):
    HOME_TYPES = (
        ('Apartment', 'Apartment'),
        ('Duplex', 'Duplex'),
        ('VacantResidentialLand', 'Vacant Residential Land'),
        ('Miscellaneous', 'Miscellaneous'),
        ('SingleFamily', 'Single Family'),
        ('MultiFamily2To4', 'Multi Family (2 to 4 people)'),
        ('Condominium', 'Condominium'),
    )
    area_unit = models.CharField(max_length=50)
    bathrooms = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    bedrooms = models.IntegerField()
    home_size = models.IntegerField()
    home_type = models.CharField(max_length=50, choices=HOME_TYPES)
    last_sold_date = models.DateTimeField(blank=True, null=True)
    last_sold_price = models.IntegerField(blank=True, null=True)
    link = models.TextField()
    price = models.TextField(),
    property_size = models.IntegerField(),
    rent_price = models.IntegerField()
    rentzestimate_amount = models.IntegerField()
    rentzestimate_last_updated = models.DateTimeField(blank=True, null=True),
    tax_value = models.DecimalField(max_digits=50, decimal_places=1, null=True),
    tax_year = models.DateTimeField(blank=True, null=True)
    year_built = models.DateTimeField(blank=True, null=True)
    zestimate_amount = models.IntegerField()
    zestimate_last_updated = models.DateTimeField(blank=True, null=True),
    zillow_id = models.BigIntegerField()
    address = models.TextField()
    city = models.TextField()
    state  = models.TextField()
    zipcode  = models.TextField()
