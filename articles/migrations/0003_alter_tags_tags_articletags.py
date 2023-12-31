# Generated by Django 4.2.2 on 2023-06-14 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='articles.article', verbose_name='Тэг'),
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arc', to='articles.article')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arc', to='articles.tags')),
            ],
        ),
    ]
