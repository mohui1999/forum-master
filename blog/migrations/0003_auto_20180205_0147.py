# Generated by Django 2.0 on 2018-02-04 17:47

# import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180120_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field= ''
            # field=ckeditor.fields.RichTextField(),
        ),
    ]
