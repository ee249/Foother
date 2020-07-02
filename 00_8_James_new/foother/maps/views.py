from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def create(request):
    # user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('accounts:profile', review.user.username)

    else:
        form = ReviewForm()
        # key = config('API_KEY')

    context = {
        'form' : form,
        # 'key' : key,
    }
    return render(request, 'maps/review_create.html', context)


@login_required
def like(request, pk):
    user = request.user
    review = get_object_or_404(Review, pk=pk)
    # user.like_posts => user가 좋아요 버튼을 누른 게시물들
    # post.like_users => post에 좋아요 버튼을 누른 유저들
    if review in user.like_reviews.all():
        # 이미 누른경우
        user.like_reviews.remove(review)
        liked = False
    else:
        # 아직 안누른경우
        user.like_reviews.add(review)
        liked = True
    # return redirect('posts:index')

    context = {
        'msg':'좋아요기능이 동작했습니다.',
        'liked':liked
    }
    return JsonResponse(context)