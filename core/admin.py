from django.contrib import admin
from .models import Clientes, Escrituraria, Bombeiro, TipoExtintor, DadosCadastrais, Socios


# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['pasta', 'cliente', 'fantasia', 'cnpj_cpf', 'Fk_Escrituraria']


@admin.register(Escrituraria)
class EscriturariaAdmin(admin.ModelAdmin):
    list_display = ['escrituraria']


@admin.register(TipoExtintor)
class TipoExtintorAdmin(admin.ModelAdmin):
    list_display = ['tipo_extintor']


@admin.register(Bombeiro)
class BombeiroAdmin(admin.ModelAdmin):
    list_display = ['fk_cliente', 'cod', 'vencimento', 'ano', 'status', 'andamento',
                    'area', 'fk_extintor', 'anotacoes', 'termo', 'sd']


@admin.register(DadosCadastrais)
class DadosCadastraisAdmin(admin.ModelAdmin):
    list_display = ['fk_cliente', 'Capital', 'insc_municipal', 'insc_estadual', 'nire_atual', 'data_ult_alteracao',
                    'inicio_lux', 'logradouro', 'numero', 'bairro', 'cep', 'cidade', 'estado', 'regime',
                    'enquadramento', 'data_abertura', 'nire_anterior']


@admin.register(Socios)
class SociosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'rg', 'cpf', 'nascimento', 'participacao', 'porcentagem', 'logradouro', 'numero',
                    'bairro', 'cep', 'cidade', 'estado']
