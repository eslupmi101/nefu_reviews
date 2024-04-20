from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Review, User, UserTelegram


def index(request):
    telegram_id = request.GET.get('telegram_id')

    if telegram_id and UserTelegram.objects.filter(id=telegram_id).exists():
        user_telegram = UserTelegram.objects.get(id=telegram_id)

        if not User.objects.filter(user_telegram__id=telegram_id).exists():
            user = User.objects.create_user(
                username=telegram_id,
                user_telegram=user_telegram
            )
            user.user_telegram = user_telegram

        user = User.objects.get(user_telegram__id=telegram_id)
        login(request, user)

    reviews_list = Review.objects.all().order_by('-likes')
    template = 'index.html'
    context = {
        'user': request.user,
        'reviews_list': reviews_list
    }

    return render(request, template, context)


@login_required
def like_review(request, review_id):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_id)
        review.likes += 1
        review.save()
    return redirect('reviews:index')
