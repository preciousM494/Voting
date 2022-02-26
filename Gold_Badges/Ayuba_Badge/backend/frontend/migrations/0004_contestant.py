# Generated by Django 4.0.2 on 2022-02-10 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_userprofile_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('office', models.CharField(choices=[('President', 'President'), ('Governor', 'Governor'), ('Senator', 'Senator'), ('House of Reprentatives', 'House of Representatives'), ('House of Assembly', 'House of Assembly'), ('Local Government Chairman', 'Local Government Chairman'), ('Councelor', 'Councelor')], max_length=100)),
                ('contestant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.userprofile')),
            ],
        ),
    ]