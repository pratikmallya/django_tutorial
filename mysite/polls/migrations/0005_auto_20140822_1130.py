# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20140822_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='polls',
            new_name='votes',
        ),
    ]
