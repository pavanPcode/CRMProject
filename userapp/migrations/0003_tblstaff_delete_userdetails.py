# Generated by Django 4.2.5 on 2023-09-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_userdetails_email_alter_userdetails_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tblstaff',
            fields=[
                ('staffid', models.AutoField(db_column='staffid', primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='email', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tblstaff',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
