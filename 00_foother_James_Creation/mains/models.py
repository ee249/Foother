from django.db import models

# Create your models here.
class Emotion(models.Model):
    emotion_name = models.CharField(max_length=100) 
    # selectbox로 설정
    # img = models.ImageField()
    # food_set 자동생김    


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    # food_by_emotion

