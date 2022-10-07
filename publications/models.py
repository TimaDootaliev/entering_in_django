from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Publication(models.Model):
    STATUS_CHOICES = (
        ('open', 'Открытая'),
        ('closed', 'Закрытая'),
        ('draft', 'Черновик')
    )
    """  
    Классы. которые наследуются от models.Model являются моделями - представление таблицы в БД
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='pubs', null=True) # null - в БД хранится NULL
    text = models.TextField(blank=True) # blank - поле становится необязательным к заполнению, в БД хранит пустую строку
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    # User.publications.all()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.title} from {self.user.username}'


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at'] # сортировка по указанным полям, "-" в начале названия означает сортировку по убыванию
