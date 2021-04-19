# Generated by Django 3.2 on 2021-04-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_decision_admitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='admitted',
            field=models.CharField(choices=[('ADMIT', 'Admitted'), ('WAITLIST', 'Waitlisted'), ('WAITLIST_ADMIT', 'Waitlist-Admitted'), ('WAITLIST_DENY', 'Waitlist-Denied'), ('DEFER', 'Deferred'), ('DEFER_ADMIT', 'Deferred-Admitted'), ('DEFER_DENY', 'Deferred-Denied'), ('DENY', 'Denied')], default='DENY', max_length=20),
        ),
    ]
