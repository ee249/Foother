from django.shortcuts import render
from .models import Food, Emotion

# Create your views here.
def main(request):
    emotions = Emotion.objects.all()
    # emotion = Emotion.objects.get(name=Food.food_name).emotion
    # foods = emotion.food_set.all()

    context = {
        'emotions' : emotions,
        # 'foods' : foods
    }
    return render(request,'foother/main.html', context)


def result(request, emotion_id):
    emotion = Emotion.objects.get(pk=emotion_id)
    foods = emotion.food_set.all()
    # emotion에 pk가 emotion_id인 emotion을 가지고 온다.
    # 그 emotion에 음식 세트를 모두 가져온다.
    context = {
        'foods' : foods,
    }
    return render(request,'foother/result.html', context)
    # 예상 food.emotion_

def select(request, food_name):
    food = Food.objects.get(food_name=food_name)
    context = {
        'food' : food,
    }
    return render(request, 'foother/select.html', context)
   

def example(request):
    return render(request, 'foother/example.html')
