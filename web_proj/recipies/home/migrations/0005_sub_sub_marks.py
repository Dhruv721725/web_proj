# Generated by Django 4.2.6 on 2024-01-05 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_student_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='st_marks', to='home.student')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sub')),
            ],
            options={
                'unique_together': {('st', 'sub')},
            },
        ),
    ]
