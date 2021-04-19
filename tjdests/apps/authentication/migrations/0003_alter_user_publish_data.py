# Generated by Django 3.2 on 2021-04-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='publish_data',
            field=models.BooleanField(default=False, help_text='Unless this is set, your data will not appear publicly.', verbose_name='Publish my data'),
        ),
    ]
