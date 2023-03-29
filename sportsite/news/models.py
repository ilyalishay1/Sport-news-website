from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey('ArticleCategory', on_delete=models.PROTECT, verbose_name='Категория')
    football_category = models.ForeignKey('FootballCategory', on_delete=models.PROTECT, verbose_name='Футбольный Чемпионат', null=True)
    basketball_category = models.ForeignKey('BasketballCategory', on_delete=models.PROTECT, verbose_name='Баскетбольный Чемпионат', null=True)
    hockey_category = models.ForeignKey('HockeyCategory', on_delete=models.PROTECT, verbose_name='ХоккейныйЧемпионат', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']


class ArticleCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True,verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class FootballCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Футбольный Чемпионат')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Футбольный Чемпионат'
        verbose_name_plural = 'Футбольные Чемпионаты'


class BasketballCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Бакстебольный чемпионат')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бакстебольный чемпионат'
        verbose_name_plural = 'Бакстебольные чемпионаты'


class HockeyCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Хоккейный чемпионат')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хоккейный чемпионат'
        verbose_name_plural = 'Хоккейные чемпионаты'
