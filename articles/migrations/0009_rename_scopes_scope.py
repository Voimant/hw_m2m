# Generated by Django 4.2.2 on 2023-06-14 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_tag_article_tags_rename_tags_scopes_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scopes',
            new_name='Scope',
        ),
    ]
