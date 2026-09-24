from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_coustomuser_managers'),
    ]

    operations = [

        # First remove UNIQUE from email
        migrations.AlterField(
            model_name='coustomuser',
            name='email',
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
            ),
        ),

        # Then make username unique
        migrations.AlterField(
            model_name='coustomuser',
            name='username',
            field=models.CharField(
                max_length=150,
                unique=True,
            ),
        ),
    ]