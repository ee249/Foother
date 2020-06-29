from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Map(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    #뭔가 더 정해야 한다.


class Upload(models.Model):
    restaurant_address = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    food_star = models.FloatField()
    food_image = ProcessedImageField(
                upload_to='upload_photo',
                processors=[ResizeToFill(200, 200)],
                format='JPEG',
                options={
                    'quality': 80}
    )
    upload_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    