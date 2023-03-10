# Generated by Django 4.1.1 on 2023-01-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('rppid', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('paymentmode', models.IntegerField(choices=[(0, 'COD'), (1, 'Net Banking')], default=0)),
                ('paymentstatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready to Ship'), (4, 'Shipped'), (5, 'Out For Delivery'), (6, 'Delivered'), (7, 'Cancelled')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.checkout')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
    ]
