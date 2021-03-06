# Generated by Django 2.0.8 on 2018-09-12 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=1)),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='cpf',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AddField(
            model_name='post',
            name='sexo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Sexo'),
        ),
    ]
