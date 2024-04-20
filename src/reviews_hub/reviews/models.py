from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


# TODO Fix Not connect to django settings
class UserTelegram(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __repr__(self):
        return (
            f'<Review id={self.id},\n'
            f'user={self.user},\n'
            f'review={self.review},\n'
            f'created_at={self.created_at},\n'
            f'likes={self.likes}>'
        )

    class Meta:
        managed = False
        db_table = 'users'


class User(AbstractUser):
    user_telegram = models.OneToOneField(
        UserTelegram,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='django_user'
    )

    class Meta:
        db_table = 'django_users'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.TextField()
    user = models.ForeignKey(
        UserTelegram,
        on_delete=models.CASCADE
    )
    likes = models.IntegerField(default=0)
    photos = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    def __repr__(self):
        return (
            f'<Review id={self.id},\n'
            f'user={self.user},\n'
            f'review={self.review},\n'
            f'created_at={self.created_at},\n'
            f'likes={self.likes}>'
        )

    class Meta:
        managed = False
        db_table = 'reviews'
