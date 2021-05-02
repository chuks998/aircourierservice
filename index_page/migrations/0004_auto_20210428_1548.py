# Generated by Django 3.1.5 on 2021-04-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0003_auto_20210427_1838'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemMovemnt',
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='first_movement',
            field=models.CharField(default='example; Your item arrived poland wherehouse', help_text='example; Your item left qater wherehouse', max_length=100),
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='fourth_movement',
            field=models.CharField(default='example; Your item arrived poland wherehouse', help_text='example; Your item arrived spain wherehouse', max_length=100),
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='second_movement',
            field=models.CharField(default='example; Your item arrived poland wherehouse', help_text='example; Your item arrived poland wherehouse', max_length=100),
        ),
        migrations.AddField(
            model_name='packagedetail',
            name='third_movement',
            field=models.CharField(default='example; Your item arrived poland wherehouse', help_text='example; Your item left lagos wherehouse', max_length=100),
        ),
        migrations.AlterField(
            model_name='packagedetail',
            name='status',
            field=models.CharField(choices=[('delayed', 'delayed'), ('delivered', 'delivered'), ('pending', 'pending'), ('active', 'active')], default=1, help_text='This section shows the client the status of their item', max_length=11),
        ),
    ]
