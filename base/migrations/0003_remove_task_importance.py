from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='importance',
        ),
    ]
