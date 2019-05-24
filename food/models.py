from django.db import models

# Create your models here.
from django.db.models import Count


class Food(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='名称')
    author = models.CharField(max_length=50,
                              verbose_name='作者')
    steps = models.CharField(verbose_name='步数', max_length=20)
    steps_time = models.CharField(verbose_name='时间', max_length=20)
    practice = models.CharField(verbose_name='做法', max_length=20)
    taste = models.CharField(verbose_name='口味', max_length=20)
    image = models.CharField(verbose_name='图片', max_length=200,
                             blank=True,
                             null=True)

    @property
    def post_cnt(self):
        return FoodPost.objects.filter(food_id=self.id).aggregate(Count('id'))

    @property
    def star_cnt(self):
        return FoodStar.objects.filter(food_id=self.id).aggregate(Count('id'))

    class Meta:
        db_table = 't_food'
        indexes = [models.Index(fields=('name', ))]


class FoodPost(models.Model):
    food_id = models.IntegerField(verbose_name='食物ID')
    user_id = models.IntegerField(verbose_name='用户ID')
    follow_post_id = models.IntegerField(verbose_name='跟帖ID', default=0)
    content = models.TextField(verbose_name='回帖内容')

    class Meta:
        db_table = 't_food_post'


class AbsStar(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID')
    up_stars = models.IntegerField(verbose_name='点赞量', default=0)
    down_stars = models.IntegerField(verbose_name='倒赞量', default=0)

    class Meta:
        abstract = True


class FoodStar(AbsStar):
    food_id = models.IntegerField(verbose_name='食物ID')

    class Meta:
        db_table = 't_food_star'
        indexes = [models.Index(fields=('user_id', 'food_id'), name='index_user_food')]
        unique_together = [['user_id', 'food_id']]


class PostStar(AbsStar):
    post_id = models.IntegerField(verbose_name='回帖ID')

    class Meta:
        db_table = 't_post_star'
        indexes = [models.Index(fields=('user_id', 'post_id'), name='index_user_post')]
        unique_together = [['user_id', 'post_id']]