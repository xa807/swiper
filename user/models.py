from django.db import models


# Create your models here.
class User(models.Model):
    sexs = ((0, '男'),
            (1, '女'))

    phonenum = models.CharField(max_length=30,
                                verbose_name='手机号码',
                                unique=True, )

    nickname = models.CharField(max_length=30, verbose_name='昵称')
    sex = models.IntegerField(choices=sexs, verbose_name='性别', default=0)

    @property
    def sex_label(self):
        return self.sexs[self.sex]

    avatar = models.CharField(max_length=200,
                              verbose_name='头像', blank=True, null=True)
    location = models.CharField(max_length=100,
                                verbose_name='坐标', null=True, blank=True)

    added = models.DateTimeField(verbose_name='申请时间',
                                 auto_now_add=True)

    modified = models.DateTimeField(verbose_name='更新时间',
                                    auto_now=True)

    def __str__(self):
        return self.phonenum

    class Meta:
        db_table = 't_user'
