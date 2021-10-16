from django.contrib import admin
from .models import Clientes, Escrituraria, Socios


# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['pasta', 'cliente', 'cnpj_cpf', 'Capital', 'insc_municipal', 'insc_estadual',
                    'nire_atual', 'data_ult_alteracao', 'inicio_lux', 'logradouro', 'numero', 'bairro', 'cep',
                    'cidade', 'estado', 'regime', 'enquadramento', 'Fk_Escrituraria', 'data_abertura', 'nire_anterior']


@admin.register(Escrituraria)
class EscriturariaAdmin(admin.ModelAdmin):
    list_display = ['escrituraria']


@admin.register(Socios)
class SociosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rg', 'cpf', 'nascimento', 'participacao', 'porcentagem', 'logradouro', 'numero',
                    'bairro', 'cep', 'cidade', 'estado']




