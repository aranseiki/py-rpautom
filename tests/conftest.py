from pytest import fixture

from py_rpautom.desktop_utils import (
    _aplicacao,
    capturar_texto,
    clicar,
    coletar_dado_selecionado,
    coletar_dados_selecao,
    coletar_situacao_janela,
    digitar,
    encerrar_app,
    esta_visivel,
    fechar_janela,
    iniciar_app,
    _localiza_elemento,
    maximizar_janela,
    minimizar_janela,
    restaurar_janela,
    selecionar_em_campo_selecao,
    selecionar_menu,
)
from py_rpautom.python_utils import (
    caminho_existente,
    criar_arquivo_texto,
    criar_pasta,
    excluir_arquivo,
    excluir_pasta,
    caminho_existente,
)


@fixture
def _aplicacao_test():
    return _aplicacao()


@fixture
def executavel_mouseclicker():
    executavel_path = 'tests/mouseclicker.exe'
    return executavel_path


@fixture
def executavel_notepad():
    executavel_path = 'notepad'
    return executavel_path


@fixture
def caminho_campo():
    caminho_campo = 'Free Mouse Clicker->Start'
    return caminho_campo


@fixture
def valor():
    valor = 5
    return valor


@fixture
def iniciar_app_test(executavel_mouseclicker):
    return iniciar_app(executavel_mouseclicker)


@fixture
def encerrar_app_test(executavel_mouseclicker):
    encerrar_app(executavel_mouseclicker)
    return True


@fixture
def contexto_mouseclicker(executavel_mouseclicker):
    app = iniciar_app(executavel_mouseclicker)
    yield app
    encerrar_app(executavel_mouseclicker)
    return app


@fixture
def contexto_notepad(executavel_notepad):
    app = iniciar_app(executavel_notepad)
    yield app
    encerrar_app(executavel_notepad)
    return app


@fixture
def digitar_test(caminho_campo, valor):
    return digitar(caminho_campo, valor)


@fixture
def _localiza_elemento_estatico_test(caminho_campo):
    return _localiza_elemento(caminho_campo, estatico=True)


@fixture
def _localiza_elemento_dinamico_test(caminho_campo):
    return _localiza_elemento(caminho_campo, estatico=False)


@fixture
def capturar_texto_test(caminho_campo):
    capturar_texto(caminho_campo)


@fixture
def clicar_test(caminho_campo):
    return clicar(caminho_campo)


@fixture
def esta_visivel_test():
    nome_janela = 'Free Mouse Clicker'
    return esta_visivel(nome_janela)


@fixture
def coletar_situacao_janela_normal_test():
    nome_janela = 'Free Mouse Clicker'
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_minimizada_test():
    nome_janela = 'Free Mouse Clicker'
    minimizar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_maximizada_test():
    nome_janela = 'Free Mouse Clicker'
    maximizar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_restaurada_test():
    nome_janela = 'Free Mouse Clicker'
    maximizar_janela(nome_janela)
    restaurar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def minimizar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return minimizar_janela(nome_janela)


@fixture
def maximizar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return maximizar_janela(nome_janela)


@fixture
def restaurar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return restaurar_janela(nome_janela)


@fixture
def coletar_dados_selecao_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    return coletar_dados_selecao(caminho_campo)


@fixture
def coletar_dado_selecionado_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    return coletar_dado_selecionado(caminho_campo)


@fixture
def selecionar_em_campo_selecao_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    item = 'Single Click'
    return selecionar_em_campo_selecao(caminho_campo, item)


@fixture
def selecionar_menu_test():
    nome_janela = 'Sem título - Bloco de Notas'
    caminho_menu = '&Arquivo->Abrir'
    return selecionar_menu(nome_janela, caminho_menu)


@fixture
def fechar_janela_test():
    nome_janela = 'Sem título - Bloco de Notas'
    return fechar_janela(nome_janela)


@fixture
def caminho_pasta_exemplo():
    caminho = 'exemplo'
    return caminho


@fixture
def caminho_pasta_exemplo_2():
    caminho = 'exemplo/exemplo2'
    return caminho


@fixture
def caminho_pasta_exemplo_3():
    caminho = 'exemplo3'
    return caminho


@fixture
def caminho_pasta_exemplo_4():
    caminho = 'exemplo4'
    return caminho


@fixture
def caminho_pasta_exemplo_5():
    caminho = 'exemplo3/exemplo4'
    return caminho


@fixture
def contexto_manipulacao_pastas_vazias_excluir(caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    yield excluir_pasta(caminho)


@fixture
def contexto_manipulacao_pastas_vazias_criar(caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    criar_pasta(caminho)
    yield
    excluir_pasta(caminho, vazia=True)


@fixture
def contexto_manipulacao_pastas_cheias_criar(caminho_pasta_exemplo_2):
    caminho = caminho_pasta_exemplo_2
    yield criar_pasta(caminho)


@fixture
def contexto_manipulacao_pastas_cheias_excluir(caminho_pasta_exemplo_2):
    caminho = caminho_pasta_exemplo_2
    yield excluir_pasta(caminho, vazia=False)


@fixture
def contexto_manipulacao_pastas_renomear(
    caminho_pasta_exemplo_3, caminho_pasta_exemplo_4
):
    caminho3 = caminho_pasta_exemplo_3
    criar_pasta(caminho3)
    yield
    excluir_pasta(caminho_pasta_exemplo_4, vazia=True)


@fixture
def contexto_manipulacao_pastas_recortar(
    caminho_pasta_exemplo_3, caminho_pasta_exemplo_4, caminho_pasta_exemplo_5
):
    caminho3 = caminho_pasta_exemplo_3
    caminho4 = caminho_pasta_exemplo_4
    criar_pasta(caminho3)
    criar_pasta(caminho4)
    yield
    excluir_pasta(caminho_pasta_exemplo_3, vazia=False)
    excluir_pasta(caminho_pasta_exemplo_5)


@fixture
def contexto_manipulacao_pasta_copiar(
    caminho_pasta_exemplo, caminho_pasta_exemplo_3
):
    pasta = caminho_pasta_exemplo
    if not caminho_existente(pasta) == True:
        criar_pasta(pasta)
    caminho_destino = caminho_pasta_exemplo_3
    if not caminho_existente(caminho_destino) == True:
        criar_pasta(caminho_destino)
    yield
    excluir_pasta(pasta, vazia=True)
    excluir_pasta(caminho_destino, vazia=False)


@fixture
def contexto_manipulacao_pasta_mostar_arquivos(
    caminho_pasta_exemplo, caminho_raiz, arquivo_exemplo, arquivo_exemplo_2
):
    pasta = caminho_pasta_exemplo
    if not caminho_existente(pasta) == True:
        criar_pasta(pasta)
        criar_arquivo_texto(pasta + '/' + arquivo_exemplo)
        criar_arquivo_texto(pasta + '/' + arquivo_exemplo_2)
    yield
    excluir_pasta(pasta, vazia=False)


@fixture
def caminho_arquivo():
    caminho = './novo_arquivo_test.txt'
    return caminho


@fixture
def caminho_arquivo_2():
    caminho = 'tests/novo_arquivo_test.txt'
    return caminho


@fixture
def caminho_raiz():
    caminho = './'
    return caminho


@fixture
def arquivo_exemplo():
    arquivo = 'arquivo_test.txt'
    return arquivo


@fixture
def arquivo_exemplo_2():
    arquivo = 'arquivo_renomeado.txt'
    return arquivo


@fixture
def excluir_arquivo_test(caminho_arquivo):
    excluir_arquivo(caminho_arquivo)


@fixture
def contexto_manipulacao_arquivo_excluir(caminho_arquivo):
    caminho = caminho_arquivo
    if caminho_existente(caminho) == True:
        excluir_arquivo(caminho)
    yield
    excluir_arquivo(caminho)


@fixture
def contexto_manipulacao_arquivo_criar(caminho_arquivo):
    caminho = caminho_arquivo
    if not caminho_existente(caminho) == True:
        criar_arquivo_texto(caminho)
    yield
    excluir_arquivo(caminho)


@fixture
def contexto_manipulacao_arquivo_copiar(
    caminho_arquivo, caminho_pasta_exemplo
):
    arquivo = caminho_arquivo
    if not caminho_existente(arquivo) == True:
        criar_arquivo_texto(arquivo)
    if not caminho_existente(caminho_pasta_exemplo) == True:
        criar_pasta(caminho_pasta_exemplo)
    yield
    excluir_pasta(caminho=caminho_pasta_exemplo, vazia=False)
    excluir_arquivo(caminho=arquivo)


@fixture
def contexto_manipulacao_arquivo_criar_2(
    caminho_raiz, arquivo_exemplo, arquivo_exemplo_2
):
    caminho = caminho_raiz
    nome_arquivo = arquivo_exemplo
    novo_nome = arquivo_exemplo_2
    if not caminho_existente(nome_arquivo) == True:
        criar_arquivo_texto(caminho + nome_arquivo)
    yield
    excluir_arquivo(caminho + novo_nome)


@fixture
def contexto_manipulacao_arquivo_criar_3(caminho_arquivo, caminho_arquivo_2):
    caminho_atual = caminho_arquivo
    caminho_novo = caminho_arquivo_2
    if not caminho_existente(caminho_atual) == True:
        criar_arquivo_texto(caminho_atual)
    yield
    excluir_arquivo(caminho_novo)
