# Generated by Django 4.1.6 on 2023-02-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AR', '0011_cart_imgfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('imgfile', models.ImageField(upload_to='')),
            ],
        ),
    ]
