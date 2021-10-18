from django.db import models


# Create your models here.
class Clientes(models.Model):
    pasta = models.IntegerField()
    cliente = models.CharField('Cliente', max_length=100)
    fantasia = models.CharField('Nome Fantasia', max_length=100, blank=True)
    cnpj_cpf = models.CharField('CNPJ/CPF', max_length=20)
    Fk_Escrituraria = models.ForeignKey('Escrituraria', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.cliente


class Escrituraria(models.Model):
    escrituraria = models.CharField('Escriturária', max_length=20)

    class Meta:
        verbose_name = 'Escrituraria'
        verbose_name_plural = 'Escriturarias'

    def __str__(self):
        return self.escrituraria


class DadosCadastrais(models.Model):
    fk_cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    Capital = models.FloatField('Capital Social', blank=True, default=0)
    FK_Socios = models.ManyToManyField('Socios')  # relacionamento muitos para muitos
    insc_municipal = models.CharField('CMC', max_length=20, blank=True)
    insc_estadual = models.CharField('Inscrição Estadual', max_length=20, blank=True)
    nire_atual = models.CharField('Nire Atual', max_length=20, blank=True)
    data_ult_alteracao = models.CharField('Data Ultima Alteração', max_length=10, blank=True)
    inicio_lux = models.CharField('Inicio Lux', max_length=10, blank=True)
    logradouro = models.CharField('logradouro', max_length=100, blank=True)
    numero = models.CharField('Numero', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=50, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True)
    estado = models.CharField('Estado', max_length=10, blank=True)
    regime = models.CharField('Regime', max_length=20, blank=True)
    enquadramento = models.CharField('Enquadramento', max_length=10, blank=True)
    data_abertura = models.CharField('Data de Abertura', max_length=10, blank=True)
    nire_anterior = models.CharField('Nire Anterior', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Dado Cadastral'
        verbose_name_plural = 'Dados Cadastrais'


class Socios(models.Model):
    nome = models.CharField('Sócio', max_length=50)
    rg = models.CharField('RG', max_length=20, blank=True)
    cpf = models.CharField('CPF', max_length=20)
    nascimento = models.DateField('Data de Nascimento', blank=True)
    participacao = models.FloatField('Participação', max_length=20, blank=True)
    porcentagem = models.CharField('Porcentagem', max_length=10, blank=True)
    logradouro = models.CharField('Logradouro', max_length=50, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=50, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True)
    estado = models.CharField('Estado', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return self.nome


class TipoExtintor(models.Model):
    tipo_extintor = models.CharField('Tipo Extintor', max_length=200)

    class Meta:
        verbose_name = 'Extintor'
        verbose_name_plural = 'Extintores'

    def __str__(self):
        return self.tipo_extintor


class Bombeiro(models.Model):
    fk_cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    cod = models.IntegerField('Codigo Bombeiro')
    vencimento = models.DateField('Vencimento')
    ano = models.CharField('Ano', max_length=4, blank=True)
    status = models.CharField('Status', max_length=100, blank=True)
    andamento = models.CharField('Andamento', max_length=100, blank=True)
    area = models.FloatField('Area', default=0)
    fk_extintor = models.ForeignKey('TipoExtintor', on_delete=models.CASCADE)
    anotacoes = models.CharField('Anotações', max_length=100, blank=True)
    termo = models.CharField('Termo', max_length=100, blank=True)
    sd = models.CharField('SD', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Bombeiro'
        verbose_name_plural = 'Bombeiros'
