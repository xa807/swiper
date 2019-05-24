# Generated by Django 2.2.1 on 2019-05-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('steps', models.CharField(max_length=20, verbose_name='步数')),
                ('steps_time', models.CharField(max_length=20, verbose_name='时间')),
                ('practice', models.CharField(max_length=20, verbose_name='做法')),
                ('taste', models.CharField(max_length=20, verbose_name='口味')),
            ],
            options={
                'db_table': 't_food',
            },
        ),
        migrations.CreateModel(
            name='FoodPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField(verbose_name='食物ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('follow_post_id', models.IntegerField(default=0, verbose_name='跟帖ID')),
                ('content', models.TextField(verbose_name='回帖内容')),
            ],
            options={
                'db_table': 't_food_post',
            },
        ),
        migrations.CreateModel(
            name='FoodStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('up_stars', models.IntegerField(default=0, verbose_name='点赞量')),
                ('down_stars', models.IntegerField(default=0, verbose_name='倒赞量')),
                ('food_id', models.IntegerField(verbose_name='食物ID')),
            ],
            options={
                'db_table': 't_food_star',
            },
        ),
        migrations.CreateModel(
            name='PostStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('up_stars', models.IntegerField(default=0, verbose_name='点赞量')),
                ('down_stars', models.IntegerField(default=0, verbose_name='倒赞量')),
                ('post_id', models.IntegerField(verbose_name='回帖ID')),
            ],
            options={
                'db_table': 't_post_star',
            },
        ),
        migrations.AddIndex(
            model_name='poststar',
            index=models.Index(fields=['user_id', 'post_id'], name='index_user_post'),
        ),
        migrations.AlterUniqueTogether(
            name='poststar',
            unique_together={('user_id', 'post_id')},
        ),
        migrations.AddIndex(
            model_name='foodstar',
            index=models.Index(fields=['user_id', 'food_id'], name='index_user_food'),
        ),
        migrations.AlterUniqueTogether(
            name='foodstar',
            unique_together={('user_id', 'food_id')},
        ),
        migrations.AddIndex(
            model_name='food',
            index=models.Index(fields=['name'], name='t_food_name_303cac_idx'),
        ),
    ]
