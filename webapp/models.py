from django.db import models
# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=255)
    brand_name = models.TextField()
    # desc = models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="images") 

    def __str__(self):
        return self.title