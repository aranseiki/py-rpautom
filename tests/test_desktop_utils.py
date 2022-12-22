from pytest import fixture, mark
from pywinauto import Application, application

from py_rpautom.python_utils import *
from tests.conftest import (
    aplicacao_test,
    clicar_test,
    contexto_mouseclicker,
    contexto_notepad,
    executavel_mouseclicker,
    iniciar_app_test,
    _localizar_elemento,
)


@mark.mouseclicker
def test_quando_o_objeto_application_for_iniciado_o_mesmo_deve_retornar_um_objeto_tipo_application(
    aplicacao_test,
):
    app_esperado = type(Application())
    app = aplicacao_test
    app_test = type(app)
    assert app_test == app_esperado


@mark.mouseclicker
def test_quando_a_aplicacao_iniciar_deve_retornar_um_objeto_tipo_application(
    contexto_mouseclicker,
):
    app_esperado = type(Application())
    app = contexto_mouseclicker
    app_test = type(app)
    assert app_test == app_esperado


@mark.mouseclicker
def test_quando_a_aplicacao_iniciar_o_caminho_do_objeto_application_deve_ser_igual_ao_informado(
    executavel_mouseclicker, contexto_mouseclicker
):
    from pathlib import Path

    caminho = str(Path(executavel_mouseclicker).absolute())
    app = contexto_mouseclicker
    assert application.process_module(app.process) == caminho


@mark.mouseclicker
def test_quando_a_aplicacao_encerrar_deve_finalizar_o_processo(
    iniciar_app_test, encerrar_app_test
):
    iniciar_app_test
    app_encerrado = encerrar_app_test
    assert app_encerrado == True


@mark.mouseclicker
def test_quando_procurar_por_um_elemento_deve_retornar_um_elemento_estatico(
    caminho_campo, contexto_mouseclicker, _localizar_elemento_estatico_test
):
    elemento_localizado = _localizar_elemento_estatico_test
    caminho = caminho_campo
    campo = caminho.split('->')
    ultimo_campo = campo[-1]
    ultimo_campo = ultimo_campo.split()
    if ultimo_campo == elemento_localizado.texts():
        elemento_localizado_test = True
    assert elemento_localizado_test == True


@mark.mouseclicker
def test_quando_procurar_por_um_elemento_deve_retornar_um_elemento_dinamico(
    caminho_campo, contexto_mouseclicker, _localizar_elemento_dinamico_test
):
    elemento_localizado = _localizar_elemento_dinamico_test
    caminho = caminho_campo
    campo = caminho.split('->')
    ultimo_campo = campo[-1]
    ultimo_campo = ultimo_campo.split()
    if ultimo_campo != elemento_localizado.texts():
        elemento_localizado_test = True
    assert elemento_localizado_test == True


@mark.mouseclicker
def test_quando_o_campo_minutes_receber_um_valor_o_mesmo_campo_deve_retornar_o_valor_informado(
    contexto_mouseclicker, digitar_test
):
    valor = 5
    campo_minutes = digitar_test
    assert campo_minutes == valor


@mark.mouseclicker
def test_quando_clicar_em_um_botao_deve_retornar_verdadeiro(
    contexto_mouseclicker, clicar_test
):
    retorno_clique = clicar_test
    assert retorno_clique == True


@mark.mouseclicker
def test_quando_a_aplicacao_estiver_visivel_deve_retornar_verdadeiro(
    contexto_mouseclicker, esta_visivel_test
):
    visivel = esta_visivel_test
    if visivel == 'visivel':
        visivel = True
    assert visivel == True


@mark.mouseclicker
def test_quando_a_janela_estiver_normal_deve_retornar_estado_normal(
    contexto_mouseclicker, coletar_situacao_janela_normal_test
):
    situacao = coletar_situacao_janela_normal_test
    assert situacao == 'normal'


@mark.mouseclicker
def test_quando_a_janela_estiver_minimizado_deve_retornar_estado_minimizado(
    contexto_mouseclicker, coletar_situacao_janela_minimizada_test
):
    situacao = coletar_situacao_janela_minimizada_test
    # breakpoint()
    assert situacao == 'minimizado'


@mark.mouseclicker
def test_quando_a_janela_estiver_maximizada_deve_retornar_estado_maximizada(
    contexto_mouseclicker, coletar_situacao_janela_maximizada_test
):
    situacao = coletar_situacao_janela_maximizada_test
    # breakpoint()
    assert situacao == 'maximizado'


@mark.mouseclicker
def test_quando_minimizar_janela_deve_retornar_true(
    contexto_mouseclicker, minimizar_janela_test
):
    situacao = minimizar_janela_test
    assert situacao == True


@mark.mouseclicker
def test_quando_maximizar_janela_deve_retornar_true(
    contexto_mouseclicker, maximizar_janela_test
):
    situacao = maximizar_janela_test
    assert situacao == True


@mark.mouseclicker
def test_quando_restaurar_janela_deve_retornar_true(
    contexto_mouseclicker, restaurar_janela_test
):
    situacao = restaurar_janela_test
    assert situacao == True


@mark.mouseclicker
def test_quando_coletar_dados_do_campo_de_selecao_deve_retornar_os_valores_disponviveis_para_selecao(
    contexto_mouseclicker, coletar_dados_selecao_test
):
    dados_selecao = coletar_dados_selecao_test
    assert dados_selecao == ['Single Click', 'Double Click']


@mark.mouseclicker
def test_quando_coletar_o_dado_ja_selecionado_do_campo_de_selecao_deve_retornar_o_valor_coletado(
    contexto_mouseclicker, coletar_dado_selecionado_test
):
    dados_selecao = coletar_dado_selecionado_test
    assert dados_selecao == 'Single Click'


@mark.mouseclicker
def test_quando_selecionar_um_dado_do_campo_de_selecao_deve_retornar_o_texto_do_item_selecionado(
    contexto_mouseclicker, selecionar_em_campo_selecao_test
):
    dados_selecao = selecionar_em_campo_selecao_test
    assert dados_selecao == 'Single Click'


@mark.notepad
@mark.xfail(
    coletar_idioma_so() != 'pt_BR',
    reason='teste escrito apenas para aplicação em português',
)
def test_quando_selecionar_o_menu_informado_deve_retornar_verdadeiro(
    contexto_notepad, selecionar_menu_test
):
    menu_selecionado = selecionar_menu_test
    return menu_selecionado == True


@mark.notepad
@mark.xfail(
    coletar_idioma_so() != 'pt_BR',
    reason='teste escrito apenas para aplicação em português',
)
def test_quando_fechar_a_janela_informada_deve_retornar_verdadeiro(
    contexto_notepad, selecionar_menu_test, fechar_janela_test
):
    janela_fechada = fechar_janela_test
    return janela_fechada == True
