# Generated by Django 2.0.1 on 2018-05-01 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('champion_id', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChampionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_id', models.IntegerField(unique=True)),
                ('difficulty', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('magic', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChampionMastery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest_granted', models.BooleanField(default=False)),
                ('champion_level', models.IntegerField()),
                ('champion_points', models.IntegerField()),
                ('champion_id', models.BigIntegerField()),
                ('summoner_id', models.BigIntegerField()),
                ('champion_points_until_next_level', models.BigIntegerField()),
                ('tokens_earned', models.IntegerField()),
                ('champion_points_since_last_level', models.BigIntegerField()),
                ('last_play_time', models.DateTimeField()),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ChampionStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_id', models.BigIntegerField(unique=True)),
                ('armorperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hpperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('attackdamage', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mpperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('attackspeedoffset', models.DecimalField(decimal_places=3, max_digits=10)),
                ('armor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hpregenperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('spellblock', models.DecimalField(decimal_places=3, max_digits=10)),
                ('attackrange', models.DecimalField(decimal_places=3, max_digits=10)),
                ('movespeed', models.DecimalField(decimal_places=3, max_digits=10)),
                ('attackdamageperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mpregenperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mp', models.DecimalField(decimal_places=3, max_digits=10)),
                ('spellblockperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('crit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mpregen', models.DecimalField(decimal_places=3, max_digits=10)),
                ('attackspeedperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('hpregen', models.DecimalField(decimal_places=3, max_digits=10)),
                ('critperlevel', models.DecimalField(decimal_places=3, max_digits=10)),
                ('version', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ChampionTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='summoner',
            name='account_id',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='summoner_id',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='summoner_level',
            field=models.BigIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='summoner',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='championtag',
            unique_together={('champion_id', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='championmastery',
            unique_together={('summoner_id', 'champion_id')},
        ),
    ]
