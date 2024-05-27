# Generated by Django 4.2 on 2024-05-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0003_alter_society_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='total_buildings',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='type',
            field=models.CharField(choices=[('Bungalow', 'Bungalow'), ('Building', 'Building'), ('Both', 'Both')], default='Building', max_length=10),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societies.society')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Society', to='societies.society')),
            ],
        ),
    ]
