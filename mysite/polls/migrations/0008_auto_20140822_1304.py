# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20140822_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='text',
            new_name='choice_text',
        ),
    ]
