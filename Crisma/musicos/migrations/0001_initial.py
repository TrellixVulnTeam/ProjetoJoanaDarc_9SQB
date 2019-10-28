# Generated by Django 2.2.6 on 2019-10-28 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codMusica', models.IntegerField()),
                ('nomeMusica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repertorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtMissa', models.DateField()),
                ('hrMissa', models.TimeField()),
                ('tipoMusica', models.CharField(max_length=20)),
                ('musica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicos.Musica')),
            ],
        ),
    ]
