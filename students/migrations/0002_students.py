# Generated by Django 3.1.1 on 2020-09-13 23:53

from django.db import migrations


def create_data(apps, schema_editor):
    Student = apps.get_model('studens', 'Student')
    Student(name="Joe Silver", email="joe@email.com", document="22342342", phone = "00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
