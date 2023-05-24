from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


# The model of reviews to titles.
class Review(models.Model):

    # title = models.ForeignKey(
    #     'Title',
    #     on_delete=models.CASCADE,
    #     related_name='reviews',
    #     verbose_name='Произведение',
    #     null=True
    # )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(0, 'Минимальное значение 0'),
            MaxValueValidator(10, 'Максимальное значение 10')
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ('pub_date', )
        verbose_name = 'Комментарий к произведению',
        verbose_name_plural = 'Комментарии к произведениям'


# The model of comments to reviews.
class Comment(models.Model):

    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='write your comment'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий к отзыву',
        verbose_name_plural = 'Комментарии к отзыву'
