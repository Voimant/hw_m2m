# Generated by Django 4.2.2 on 2023-06-14 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articletags_options_rename_tags_tags_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Тэг')),
            ],
        ),
        migrations.AlterModelOptions(
            name='articletags',
            options={'ordering': ['is_main']},
        ),
        migrations.AddField(
            model_name='articletags',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='articles', through='articles.ArticleTags', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arc', to='articles.tag', verbose_name='Тег'),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
