# Generated by Django 5.1 on 2024-08-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HOME", "0006_alter_blog_section_alter_blog_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("0", "DRAFT"), ("1", "PUBLISH")], default=0, max_length=1
            ),
        ),
    ]