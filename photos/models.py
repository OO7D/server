from django.db import models

# Create your models here.
# Create your models here.
class Photo(models.Model):
    
    
    SEASON_CHOICES= (
        ("Spring", "spring"),
        ("Summer", "summer"),
        ("Autumn", "autumn"),
        ("Winter", "winter"),
    )

    class Color(models.IntegerChoices): # 사용자에게는 "빨강"으로 보이고, DB에는 숫자대로 저장됩니다. 
        red = 0
        orange = 1
        yellow = 2
        green = 3
        peaGreen = 4
        blue = 5
        skyblue = 6
        purple = 7
        pink = 8
        brown = 9
        white = 10
        gray = 11
        black = 12
    color = models.IntegerField(choices=Color.choices)
    # color_label = ["빨강", "주황", "노랑", "초록", "연두", "파랑", "하늘", "보라", "분홍", "갈색", "하양", "회색", "검정"]
    # 순서대로 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13


    TYPE_CHOICES = (
        ("블라우스","blouse"),
        ("짧은 치마","shortSkirt"),
        ("긴 치마","longSkirt"),
        ("스웨터","sweater"),
        ("드레스","dress"),
    )

    user = models.ForeignKey(
        "users.User", related_name="photo", on_delete=models.CASCADE
    )
    closet = models.ForeignKey(
        "closets.Closet", related_name = "closet", on_delete=models.CASCADE
    )

    types = models.CharField(choices= TYPE_CHOICES, max_length = 100,blank=True) # 옷 종류 보충 필요
    season = models.CharField( 
        choices=SEASON_CHOICES, max_length = 100,blank=True
        )
    photo = models.ImageField(upload_to='images/',blank=True, null=True)
    heart = models.BooleanField()
    def __str__(self):
        return "%s의 %s색 %s %s사진" % (self.user.name, self.color, self.season, self.types)

    # recentlyRecommended과 mostRecommended