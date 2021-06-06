from django.db import models

# Create your models here.

class Closet(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    recommendClothes = models.ImageField(upload_to='images/',blank=True, null=True)
    evaluateRecommend = models.PositiveIntegerField(blank= True)

    def __str__(self):
        return "%s의 옷장" % self.user.name