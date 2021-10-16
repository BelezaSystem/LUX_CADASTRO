# Generated by Django 3.2.8 on 2021-10-15 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escrituraria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escrituraria', models.CharField(max_length=20, verbose_name='Escriturária')),
            ],
            options={
                'verbose_name': 'Escrituraria',
                'verbose_name_plural': 'Escriturarias',
            },
        ),
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Cliente')),
                ('rg', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('participacao', models.FloatField(blank=True, max_length=20, null=True, verbose_name='Participação')),
                ('porcentagem', models.CharField(blank=True, max_length=10, null=True, verbose_name='Porcentagem')),
                ('logradouro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cep', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('cidade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.IntegerField()),
                ('cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('fantasia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Fantasia')),
                ('cnpj_cpf', models.CharField(max_length=20, verbose_name='CNPJ/CPF')),
                ('Capital', models.FloatField(blank=True, null=True, verbose_name='Capital Social')),
                ('insc_municipal', models.CharField(blank=True, max_length=20, null=True, verbose_name='CMC')),
                ('insc_estadual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Estadual')),
                ('nire_atual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nire Atual')),
                ('data_ult_alteracao', models.DateField(blank=True, null=True, verbose_name='Data Ultima Alteração')),
                ('inicio_lux', models.CharField(blank=True, max_length=10, null=True, verbose_name='Inicio Lux')),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='logradouro')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=10, null=True, verbose_name='CEP')),
                ('cidade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=10, null=True, verbose_name='Estado')),
                ('regime', models.CharField(blank=True, max_length=20, null=True, verbose_name='Regime')),
                ('enquadramento', models.CharField(blank=True, max_length=10, null=True, verbose_name='Enquadramento')),
                ('data_abertura', models.DateField(blank=True, verbose_name='Data de Abertura')),
                ('nire_anterior', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nire Anterior')),
                ('Fk_Escrituraria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.escrituraria')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
