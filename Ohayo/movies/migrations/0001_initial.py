# Generated by Django 2.1.8 on 2019-05-15 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mv_key_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('key_image', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_keywords', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('code', models.TextField()),
                ('imageUrl', models.TextField()),
                ('is_like', models.TextField(blank=True, default=False)),
                ('baged_users', models.ManyToManyField(blank=True, related_name='bagging_movies', to=settings.AUTH_USER_MODEL)),
                ('keywords', models.ManyToManyField(blank=True, related_name='movies', to='movies.Keyword')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]