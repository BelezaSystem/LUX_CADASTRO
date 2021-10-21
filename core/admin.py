from django.contrib import admin
from .models import Clientes, Escrituraria, Bombeiro, DadosCadastrais, Socios


# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['pasta', 'cliente', 'fantasia', 'cnpj_cpf']


@admin.register(Escrituraria)
class EscriturariaAdmin(admin.ModelAdmin):
    list_display = ['escrituraria']


@admin.register(Bombeiro)
class BombeiroAdmin(admin.ModelAdmin):
    list_display = ['fk_cliente', 'cod', 'vencimento', 'dias', 'ano', 'andamento',
                    'area', 'tp_extintores', 'anotacoes', 'termo', 'sd']


@admin.register(DadosCadastrais)
class DadosCadastraisAdmin(admin.ModelAdmin):
    list_display = ['fk_cliente', 'Capital', 'insc_municipal', 'insc_estadual', 'nire_atual', 'data_ult_alteracao',
                    'inicio_lux', 'logradouro', 'numero', 'bairro', 'cep', 'cidade', 'estado','Fk_Escrituraria', 'regime',
                    'enquadramento', 'data_abertura', 'nire_anterior']


@admin.register(Socios)
class SociosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rg', 'cpf', 'nascimento', 'participacao', 'porcentagem', 'logradouro', 'numero',
                    'bairro', 'cep', 'cidade', 'estado']
