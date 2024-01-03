# Generated by Django 4.2.8 on 2024-01-02 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(default='Without comment')),
                ('grade', models.CharField(choices=[('1', 'Worse'), ('2', 'Bad'), ('3', 'not Bad'), ('4', 'Fine'), ('5', 'Great')], default=('5', 'Great'), max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.book')),
            ],
        ),
    ]