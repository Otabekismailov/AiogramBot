# Generated by Django 4.2.4 on 2023-08-21 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_category_alter_djangocourse_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djangocourse',
            name='video',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='apps.category'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(upload_to='videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_video', to='apps.djangocourse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
