# Generated by Django 2.1.5 on 2019-03-19 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articlelikesdislikes',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='articlelikesdislikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_articles', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='article',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_articles', to='profiles.Profile'),
        ),
    ]
