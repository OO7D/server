from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    # 사용자에게는 "male"로, DB에는 0으로 저장됩니다. female도 마찬가지입니다.

    # max_length 필수, if this is True, it is allowed to be null
    class Gender(models.IntegerChoices): # 사용자에게는 "빨강"으로 보이고, DB에는 숫자대로 저장됩니다. 
        male = 0
        female = 1
    gender = models.IntegerField(choices=Gender.choices)
 
    name = models.CharField(help_text="이름을 적어주세요.", max_length=255, blank=False, null=False)
    age = models.PositiveIntegerField(help_text="나이를 적어주세요.", blank=False, null=False)

    recentlyRecommended = models.ImageField(upload_to='images/',blank=True, null=True)
    mostRecommended = models.ImageField(upload_to='images/',blank=True, null=True)
    
    mindTestResult = models.TextField()
    preferenceTestResult = models.TextField()
    def __str__(self):
        return "%s" % self.name
