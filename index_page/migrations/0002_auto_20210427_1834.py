# Generated by Django 2.2.7 on 2021-04-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedetail',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('delayed', 'delayed'), ('delivered', 'delivered'), ('pending', 'pending')], default=1, help_text='This section shows the client the status of their item', max_length=11),
        ),
    ]