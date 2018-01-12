# Generated by Django 2.0 on 2018-01-12 00:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DzienTygodnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GrupaZajeciowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czyuruchomiona', models.BooleanField()),
                ('liczbamiejsc', models.IntegerField()),
                ('liczbauczestnikow', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wartoscgodzinowa', models.IntegerField()),
                ('ects', models.IntegerField()),
                ('nazwakursu', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NauczycielAkademicki',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('liczbagodzin', models.IntegerField()),
                ('pensum', models.IntegerField()),
                ('jestpelnomocnikiem', models.BooleanField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.CharField(max_length=2500)),
                ('opiekun', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ekurser.NauczycielAkademicki')),
            ],
        ),
        migrations.CreateModel(
            name='RodzajGrupy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StatusWniosku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('nrindeksu', models.CharField(max_length=9, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('godzina', models.CharField(max_length=10)),
                ('sala', models.CharField(max_length=10)),
                ('dzien', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ekurser.DzienTygodnia')),
            ],
        ),
        migrations.CreateModel(
            name='WniosekOUruchomienieGrupyZajeciowej',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zgodapelnomocnika', models.NullBooleanField()),
                ('nrwniosku', models.CharField(max_length=10)),
                ('statuswniosku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ekurser.StatusWniosku')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ekurser.Student')),
            ],
        ),
        migrations.AddField(
            model_name='kurs',
            name='opiekun',
            field=models.ManyToManyField(related_name='kurs', to='ekurser.NauczycielAkademicki'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='prowadzacy',
            field=models.ManyToManyField(related_name='kwalifikowaneKursy', to='ekurser.NauczycielAkademicki'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='zamiennik',
            field=models.ManyToManyField(related_name='_kurs_zamiennik_+', to='ekurser.Kurs'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='kurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='grupa', to='ekurser.Kurs'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='opinia',
            field=models.ManyToManyField(related_name='grupa', to='ekurser.Opinia'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='organizator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='grupa', to='ekurser.Student'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='prowadzacy',
            field=models.ManyToManyField(related_name='grupa', to='ekurser.NauczycielAkademicki'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='rodzajgrupy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ekurser.RodzajGrupy'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='student',
            field=models.ManyToManyField(related_name='grupaZajeciowa', to='ekurser.Student'),
        ),
        migrations.AddField(
            model_name='grupazajeciowa',
            name='termin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zajecia', to='ekurser.Termin'),
        ),
    ]
