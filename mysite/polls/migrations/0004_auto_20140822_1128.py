# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='polls',
            field=models.IntegerField(default=''),
            preserve_default=True,
        ),
    ]
