from django.db import models

class JejuTouristSpot(models.Model):
    contents_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    road_address = models.CharField(max_length=255, null=True)
    tag = models.CharField(max_length=255, null=True)
    introduction = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    postcode = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    image_url = models.CharField(max_length=255, null=True)
    image_description = models.CharField(max_length=255, null=True)
    all_tag = models.TextField(null=True)

    def __str__(self):
        return self.title
