"""Módulo para automação web."""
from py_rpautom import desktop_utils as desktop_utils
from py_rpautom import python_utils as python_utils


__all__ = [
    'requisitar_url',
    'baixar_arquivo',
    'iniciar_navegador',
    'autenticar_navegador',
    'abrir_pagina',
    'abrir_pagina',
    'abrir_janela',
    'trocar_para',
    'coletar_id_janela',
    'coletar_todas_ids_janelas',
    'esperar_pagina_carregar',
    'voltar_pagina',
    'centralizar_elemento',
    'executar_script',
    'retornar_codigo_fonte',
    'aguardar_elemento',
    'procurar_muitos_elementos',
    'procurar_elemento',
    'selecionar_elemento',
    'contar_elementos',
    'extrair_texto',
    'coletar_atributo',
    'alterar_atributo',
    'clicar_elemento',
    'escrever_em_elemento',
    'limpar_campo',
    'performar',
    'print_para_pdf',
    'fechar_janela',
    'fechar_janelas_menos_essa',
    'encerrar_navegador',
]

def _coletar_tamanho(caminho):
    import os

    caminho_interno = python_utils.coletar_caminho_absoluto(caminho)

    return os.path.getsize(caminho_interno)


def _coletar_versao_navegador(caminho_arquivo):
    from win32api import GetFileVersionInfo, HIWORD, LOWORD

    caminho_interno = python_utils.coletar_caminho_absoluto(caminho_arquivo)
    informacao_arquivo = GetFileVersionInfo(caminho_interno, '\\')

    versao_major = informacao_arquivo['FileVersionMS']
    versao_minor = informacao_arquivo['FileVersionLS']

    versao_major_principal = str(HIWORD(versao_major))
    versao_major_secundario = str(LOWORD(versao_major))
    versao_minor_principal = str(HIWORD(versao_minor))
    versao_minor_secundario = str(LOWORD(versao_minor))

    versao = str('.').join(
        (
            versao_major_principal,
            versao_major_secundario,
            versao_minor_principal,
            versao_minor_secundario,
        )
    )

    return versao


def _coletar_versao_webdriver(executavel_webdriver):
    import subprocess

    execucao_webdriver = subprocess.Popen(
        [executavel_webdriver, '-V'], stdout=subprocess.PIPE
    )

    versao_webdriver = str(execucao_webdriver.stdout.read())
    versao_webdriver = versao_webdriver.partition(' (')[0]
    versao_webdriver = versao_webdriver.rpartition(' ')[-1]

    return versao_webdriver


def _preparar_ambiente(nome_navegador):
    # importa recursos dos módulos necessários
    import sys
    from collections import namedtuple

    caminho_auto_caminho = python_utils.coletar_arvore_caminho(__file__)
    pasta_projeto = python_utils.coletar_arvore_caminho(caminho_auto_caminho)
    caminho_webdriver_raiz = 'webdrivers'

    webdriver = namedtuple(
        'webdriver',
        [
            'nome',
            'versao',
            'nome_arquivo',
            'caminho',
            'tamanho',
            'plataforma',
        ],
    )

    webdriver.nome = ''
    webdriver.versao = ''
    webdriver.nome_arquivo = ''
    webdriver.caminho = ''
    webdriver.tamanho = ''
    webdriver.plataforma = ''

    if sys.platform == 'win32':
        webdriver.plataforma = 'win32'

    if nome_navegador.upper().__contains__('CHROME'):
        webdriver.nome_arquivo = 'chromedriver.exe'
        webdriver.nome = 'chromedriver'

        caminho_navegador = (
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        )
        url_base = 'https://chromedriver.storage.googleapis.com'

        lista_webdrivers = _coleta_lista_chromedrivers(url_base)

        tag_especificacao_abertura = '<Key>'
        tag_especificacao_encerramento = '</Key>'

        tag_tamanho_abertura = '<Size>'
        tag_tamanho_encerramento = '</Size>'
    elif nome_navegador.upper().__contains__('EDGE'):
        webdriver.nome_arquivo = 'msedgedriver.exe'
        webdriver.nome = 'edgedriver'

        caminho_navegador = (
            'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
        )
        url_base = 'https://msedgedriver.azureedge.net/'

        lista_webdrivers = _coleta_lista_edgedrivers(url_base)

        tag_especificacao_abertura = '<Name>'
        tag_especificacao_encerramento = '</Name>'

        tag_tamanho_abertura = '<Content-Length>'
        tag_tamanho_encerramento = '</Content-Length>'
    elif nome_navegador.upper().__contains__('FIREFOX'):
        webdriver.nome_arquivo = 'geckodriver.exe'
        webdriver.nome = 'geckodriver'
        caminho_navegador = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        url_base = 'https://github.com/mdn/content/blob/main/files/en-us/glossary/gecko/index.md?plain=1'
    else:
        raise SystemError(
            f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
        )

    webdriver.caminho = str('/').join(
        (
            pasta_projeto,
            caminho_webdriver_raiz,
            webdriver.nome,
        )
    )

    # caso o caminho existir
    if not python_utils.caminho_existente(webdriver.caminho):
        # cria a pasta informada, caso necessário
        #  cria a hierarquia anterior à última pasta
        python_utils.criar_pasta(webdriver.caminho)

    versao_navegador = _coletar_versao_navegador(caminho_navegador)

    lista_versoes = set()

    versao_sem_minor = versao_navegador[:-3]

    for grupo in lista_webdrivers.conteudo:
        especificacao = grupo[1]

        if (
            not especificacao.__contains__('.zip')
            or especificacao.__contains__('icons')
            or especificacao.__contains__('index.html')
            or especificacao.__contains__('icons/folder.gif')
            or especificacao.__contains__('LICENSE')
            or especificacao.__contains__('credits.html')
            or especificacao.__contains__('LATEST_RELEASE')
        ):
            continue

        especificacao = especificacao.removeprefix(tag_especificacao_abertura)
        especificacao = especificacao.removesuffix(
            tag_especificacao_encerramento
        )
        especificacao = especificacao.split('/')

        versao = especificacao[0]

        arquivo = especificacao[1]

        tamanho = grupo[6]
        tamanho = tamanho.removeprefix(tag_tamanho_abertura)
        tamanho = tamanho.removesuffix(tag_tamanho_encerramento)

        if versao.__contains__(versao_sem_minor):
            lista_versoes.add((versao, arquivo, tamanho))

    versoes_compativeis = []
    for versao in lista_versoes:
        versoes_compativeis.append(versao)

    versoes_compativeis.sort(reverse=True)

    for versao in versoes_compativeis:
        if (versao[0].__contains__(versao_navegador)) and (
            versao[1].__contains__(webdriver.plataforma)
        ):
            webdriver.versao = versao[0]
            arquivo_zip = versao[1]
            webdriver.tamanho = versao[2]
            break

    if webdriver.versao == '':
        for versao in versoes_compativeis:
            if versao[1].__contains__(webdriver.plataforma):
                break
        webdriver.versao = versoes_compativeis[0][0]
        arquivo_zip = versoes_compativeis[0][1]
        webdriver.tamanho = versoes_compativeis[0][2]

    url = str('/').join((url_base, webdriver.versao, arquivo_zip))

    caminho_arquivo_zip = str('/').join((webdriver.caminho, arquivo_zip))

    caminho_webdriver_pessoal = str('/').join(
        (
            webdriver.caminho,
            webdriver.versao,
        )
    )

    webdriver.caminho = python_utils.coletar_caminho_absoluto(
        caminho_webdriver_pessoal
    )

    # caso o caminho existir
    if not python_utils.caminho_existente(webdriver.caminho):
        # cria a pasta informada, caso necessário
        #  cria a hierarquia anterior à última pasta
        python_utils.criar_pasta(webdriver.caminho)

    caminho_arquivo_zip = python_utils.coletar_caminho_absoluto(caminho_arquivo_zip)

    return url, caminho_arquivo_zip, webdriver


def _coleta_lista_chromedrivers(url):
    from collections import namedtuple

    status = 0
    contagem = 0
    header_chrome = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'max-age=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    }
    while not status == 200 and contagem < 60:
        resposta = requisitar_url(url, stream=True, header_arg=header_chrome)
        status = resposta.status_code
        contagem = contagem + 1

    if not resposta.status_code in range(200, 300):
        raise SystemError(
            f'Falha ao acessar a url {url}. Revise os dados e tente novamente.'
        )

    resposta_str = str(resposta.content)
    resposta_str_dividido = resposta_str.replace('><', '>\n<')
    resposta_str_dividido = resposta_str_dividido.split('\n')

    lista_webdrivers = namedtuple(
        'lista_webdrivers', ['cabecalho', 'conteudo', 'rodape']
    )

    lista_webdrivers.cabecalho = []
    lista_webdrivers.conteudo = []
    lista_webdrivers.rodape = []

    versao_xml = resposta_str_dividido[0]
    abertura_xmlns = resposta_str_dividido[1]
    nome = resposta_str_dividido[2]
    abertura_prefix = resposta_str_dividido[3]
    encerramento_prefix = resposta_str_dividido[4]
    abertura_maker = resposta_str_dividido[5]
    encerramento_maker = resposta_str_dividido[6]
    validacao_truncado = resposta_str_dividido[7]

    lista_webdrivers.cabecalho.append(
        [
            versao_xml,
            abertura_xmlns,
            nome,
            abertura_prefix,
            encerramento_prefix,
            abertura_maker,
            encerramento_maker,
            validacao_truncado,
        ]
    )

    for item in (
        versao_xml,
        abertura_xmlns,
        nome,
        abertura_prefix,
        encerramento_prefix,
        abertura_maker,
        encerramento_maker,
        validacao_truncado,
    ):
        resposta_str_dividido.remove(item)

    encerramento_xmlns = resposta_str_dividido[-1]

    lista_webdrivers.rodape.append([encerramento_xmlns])

    resposta_str_dividido.remove(encerramento_xmlns)

    total = int(len(resposta_str_dividido) / 8)
    contagem = 0
    while contagem < total:
        abertura_contents = resposta_str_dividido[0]
        key = resposta_str_dividido[1]
        generation = resposta_str_dividido[2]
        meta_generation = resposta_str_dividido[3]
        last_modified = resposta_str_dividido[4]
        etag = resposta_str_dividido[5]
        size = resposta_str_dividido[6]
        fechamento_contents = resposta_str_dividido[7]

        for item in (
            abertura_contents,
            key,
            generation,
            meta_generation,
            last_modified,
            etag,
            size,
            fechamento_contents,
        ):
            resposta_str_dividido.remove(item)

        lista_webdrivers.conteudo.append(
            [
                abertura_contents,
                key,
                generation,
                meta_generation,
                last_modified,
                etag,
                size,
                fechamento_contents,
            ]
        )

        contagem = contagem + 1

    return lista_webdrivers


def _coleta_lista_edgedrivers(url):
    from collections import namedtuple

    status = 0
    contagem = 0
    header_edge = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'max-age=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    }
    while not status == 200 and contagem < 60:
        resposta = requisitar_url(
            url, stream=True, autenticacao=['', ''], header_arg=header_edge
        )
        status = resposta.status_code

        if status in range(200, 300):
            break
        else:
            resposta = requisitar_url(
                url,
                stream=True,
                header_arg=header_edge,
            )
            status = resposta.status_code

        contagem = contagem + 1

    if not resposta.status_code in range(200, 300):
        raise SystemError(
            f'Falha ao acessar a url {url}. Revise os dados e tente novamente.'
        )

    resposta_str = str(resposta.content)
    resposta_str_dividido = resposta_str.replace('><', '>\n<')
    resposta_str_dividido = resposta_str_dividido.split('\n')

    lista_webdrivers = namedtuple(
        'lista_webdrivers', ['cabecalho', 'conteudo', 'rodape']
    )

    lista_webdrivers.cabecalho = []
    lista_webdrivers.conteudo = []
    lista_webdrivers.rodape = []

    versao_xml = resposta_str_dividido[0]
    abertura_enumeration_results = resposta_str_dividido[1]
    abertura_blobs = resposta_str_dividido[2]

    lista_webdrivers.cabecalho.append(
        [
            versao_xml,
            abertura_enumeration_results,
            abertura_blobs,
        ]
    )

    for item in (
        versao_xml,
        abertura_enumeration_results,
        abertura_blobs,
    ):
        resposta_str_dividido.remove(item)

    encerramento_blobs = resposta_str_dividido[-3]
    encerramento_next_marker = resposta_str_dividido[-2]
    encerramento_enumeration_results = resposta_str_dividido[-1]

    lista_webdrivers.rodape.append(
        [
            encerramento_blobs,
            encerramento_next_marker,
            encerramento_enumeration_results,
        ]
    )

    for item in (
        encerramento_blobs,
        encerramento_next_marker,
        encerramento_enumeration_results,
    ):
        resposta_str_dividido.remove(item)

    total = int(len(resposta_str_dividido) / 16)
    contagem = 0

    while contagem < total:
        abertura_blob = resposta_str_dividido[0]
        name = resposta_str_dividido[1]
        url = resposta_str_dividido[2]
        properties = resposta_str_dividido[3]
        last_modified = resposta_str_dividido[4]
        e_tag = resposta_str_dividido[5]
        content_length = resposta_str_dividido[6]
        content_type = resposta_str_dividido[7]
        content_encoding = resposta_str_dividido[8]
        content_language = resposta_str_dividido[9]
        content_mds = resposta_str_dividido[10]
        cache_control = resposta_str_dividido[11]
        blob_type = resposta_str_dividido[12]
        lease_status = resposta_str_dividido[13]
        encerramento_properties = resposta_str_dividido[14]
        encerramento_blob = resposta_str_dividido[15]

        for item in (
            abertura_blob,
            name,
            url,
            properties,
            last_modified,
            e_tag,
            content_length,
            content_type,
            content_encoding,
            content_language,
            content_mds,
            cache_control,
            blob_type,
            lease_status,
            encerramento_properties,
            encerramento_blob,
        ):
            resposta_str_dividido.remove(item)

        lista_webdrivers.conteudo.append(
            [
                abertura_blob,
                name,
                url,
                properties,
                last_modified,
                e_tag,
                content_length,
                content_type,
                content_encoding,
                content_language,
                content_mds,
                cache_control,
                blob_type,
                lease_status,
                encerramento_properties,
                encerramento_blob,
            ]
        )

        contagem = contagem + 1

    return lista_webdrivers


def _escolher_tipo_elemento(tipo_elemento):
    """Escolhe um tipo de elemento 'locator'."""
    from selenium.webdriver.common.by import By

    if tipo_elemento.upper() == 'CLASS_NAME':
        tipo_elemento = By.CLASS_NAME
    elif tipo_elemento.upper() == 'CSS_SELECTOR':
        tipo_elemento = By.CSS_SELECTOR
    elif tipo_elemento.upper() == 'ID':
        tipo_elemento = By.ID
    elif tipo_elemento.upper() == 'LINK_TEXT':
        tipo_elemento = By.LINK_TEXT
    elif tipo_elemento.upper() == 'NAME':
        tipo_elemento = By.NAME
    elif tipo_elemento.upper() == 'PARTIAL_LINK_TEXT':
        tipo_elemento = By.PARTIAL_LINK_TEXT
    elif tipo_elemento.upper() == 'TAG_NAME':
        tipo_elemento = By.TAG_NAME
    elif tipo_elemento.upper() == 'XPATH':
        tipo_elemento = By.XPATH
    return tipo_elemento


def _escolher_comportamento_esperado(comportamento_esperado: str):
    """Escolhe um tipo de comportamento manipulado pelo Selenium."""
    from selenium.webdriver.support import expected_conditions as EC

    if comportamento_esperado.upper() == 'ALERT_IS_PRESENT':
        comportamento_esperado = EC.alert_is_present
    elif comportamento_esperado.upper() == 'ALL_OF':
        comportamento_esperado = EC.all_of
    elif comportamento_esperado.upper() == 'ANY_OF':
        comportamento_esperado = EC.any_of
    elif comportamento_esperado.upper() == 'ELEMENT_ATTRIBUTE_TO_INCLUDE':
        comportamento_esperado = EC.element_attribute_to_include
    elif (
        comportamento_esperado.upper()
        == 'ELEMENT_LOCATED_SELECTION_STATE_TO_BE'
    ):
        comportamento_esperado = EC.element_located_selection_state_to_be
    elif comportamento_esperado.upper() == 'ELEMENT_LOCATED_TO_BE_SELECTED':
        comportamento_esperado = EC.element_located_to_be_selected
    elif comportamento_esperado.upper() == 'ELEMENT_SELECTION_STATE_TO_BE':
        comportamento_esperado = EC.element_selection_state_to_be
    elif comportamento_esperado.upper() == 'ELEMENT_TO_BE_CLICKABLE':
        comportamento_esperado = EC.element_to_be_clickable
    elif comportamento_esperado.upper() == 'ELEMENT_TO_BE_SELECTED':
        comportamento_esperado = EC.element_to_be_selected
    elif (
        comportamento_esperado.upper()
        == 'FRAME_TO_BE_AVAILABLE_AND_SWITCH_TO_IT'
    ):
        comportamento_esperado = EC.frame_to_be_available_and_switch_to_it
    elif comportamento_esperado.upper() == 'INVISIBILITY_OF_ELEMENT':
        comportamento_esperado = EC.invisibility_of_element
    elif comportamento_esperado.upper() == 'INVISIBILITY_OF_ELEMENT_LOCATED':
        comportamento_esperado = EC.invisibility_of_element_located
    elif comportamento_esperado.upper() == 'NEW_WINDOW_IS_OPENED':
        comportamento_esperado = EC.new_window_is_opened
    elif comportamento_esperado.upper() == 'NONE_OF':
        comportamento_esperado = EC.none_of
    elif comportamento_esperado.upper() == 'NUMBER_OF_WINDOWS_TO_BE':
        comportamento_esperado = EC.number_of_windows_to_be
    elif comportamento_esperado.upper() == 'PRESENCE_OF_ALL_ELEMENTS_LOCATED':
        comportamento_esperado = EC.presence_of_all_elements_located
    elif comportamento_esperado.upper() == 'PRESENCE_OF_ELEMENT_LOCATED':
        comportamento_esperado = EC.presence_of_element_located
    elif comportamento_esperado.upper() == 'STALENESS_OF':
        comportamento_esperado = EC.staleness_of
    elif comportamento_esperado.upper() == 'TEXT_TO_BE_PRESENT_IN_ELEMENT':
        comportamento_esperado = EC.text_to_be_present_in_element
    elif (
        comportamento_esperado.upper()
        == 'TEXT_TO_BE_PRESENT_IN_ELEMENT_ATTRIBUTE'
    ):
        comportamento_esperado = EC.text_to_be_present_in_element_attribute
    elif (
        comportamento_esperado.upper() == 'TEXT_TO_BE_PRESENT_IN_ELEMENT_VALUE'
    ):
        comportamento_esperado = EC.text_to_be_present_in_element_value
    elif comportamento_esperado.upper() == 'TITLE_CONTAINS':
        comportamento_esperado = EC.title_contains
    elif comportamento_esperado.upper() == 'TITLE_IS':
        comportamento_esperado = EC.title_is
    elif comportamento_esperado.upper() == 'URL_CHANGES':
        comportamento_esperado = EC.url_changes
    elif comportamento_esperado.upper() == 'URL_CONTAINS':
        comportamento_esperado = EC.url_contains
    elif comportamento_esperado.upper() == 'URL_MATCHES':
        comportamento_esperado = EC.url_matches
    elif comportamento_esperado.upper() == 'URL_TO_BE':
        comportamento_esperado = EC.url_to_be
    elif comportamento_esperado.upper() == 'VISIBILITY_OF':
        comportamento_esperado = EC.visibility_of
    elif (
        comportamento_esperado.upper() == 'VISIBILITY_OF_ALL_ELEMENTS_LOCATED'
    ):
        comportamento_esperado = EC.visibility_of_all_elements_located
    elif (
        comportamento_esperado.upper() == 'VISIBILITY_OF_ANY_ELEMENTS_LOCATED'
    ):
        comportamento_esperado = EC.visibility_of_any_elements_located
    elif comportamento_esperado.upper() == 'VISIBILITY_OF_ELEMENT_LOCATED':
        comportamento_esperado = EC.visibility_of_element_located
    return comportamento_esperado


def _procurar_elemento(seletor, tipo_elemento='CSS_SELECTOR'):
    """Procura um elemento presente que corresponda ao informado."""
    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    webelemento = _navegador.find_element(tipo_elemento, seletor)
    centralizar_elemento(seletor, tipo_elemento)

    return webelemento


def _procurar_muitos_elementos(seletor, tipo_elemento='CSS_SELECTOR'):
    """Procura todos os elementos presentes que correspondam ao informado."""
    # instancia uma lista vazia
    lista_webelementos_str = []

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    lista_webelementos = _navegador.find_elements(tipo_elemento, seletor)
    centralizar_elemento(seletor, tipo_elemento)

    # retorna os valores coletados ou uma lista vazia
    return lista_webelementos


def requisitar_url(
    url: str,
    stream=True,
    autenticacao: None or list = None,
    header_arg: str = None,
):
    """Faz uma requisição http, retornando a resposta
    dessa requisição no padrão http/https."""
    import os
    from requests import get
    from requests.auth import HTTPBasicAuth

    verificacao_ssl = (
        os.environ['WDM_SSL_VERIFY']
    ).lower() in ['1', 1, 'true', True,]

    if autenticacao is not None:
        usuario, senha = autenticacao
        autenticacao = HTTPBasicAuth(usuario, senha)

    resposta = get(
        url,
        stream=stream,
        verify=verificacao_ssl,
        auth=autenticacao,
        headers=header_arg,
    )

    return resposta


def baixar_arquivo(
    url,
    caminho_destino,
    stream=True,
    autenticacao: None or list = None,
    header_arg=None,
) -> bool:
    """Baixa um arquivo mediante uma url do arquivo e um
    caminho de destino já com o nome do arquivo a ser gravado."""
    from shutil import copyfileobj

    caminho_interno_absoluto = python_utils.coletar_caminho_absoluto(
        caminho_destino
    )

    resposta = requisitar_url(
        url,
        stream=stream,
        autenticacao=autenticacao,
        header_arg=header_arg,
    )
    with open(caminho_interno_absoluto, 'wb') as code:
        copyfileobj(resposta.raw, code)

    return True


def validar_porta(ip, porta, tempo_limite=1):
    import socket
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.settimeout(tempo_limite)
    retorno_validacao = conexao.connect_ex((ip, porta))

    if retorno_validacao == 0:
        return True

    return False


def iniciar_navegador(
    url: str,
    nome_navegador: str,
    options: tuple = (''),
    extensoes: tuple = (''),
    experimentos: tuple = (''),
    capacidades: tuple = (''),
    executavel: str = 'padrao',
    porta_webdriver: int = None,
    baixar_webdriver_previamente: bool = True,
):
    """Inicia uma instância automatizada de um navegador."""
    import urllib3
    from selenium import webdriver
    from random import randint


    urllib3.disable_warnings()

    global _navegador
    com_extras = False


    if porta_webdriver is None:
        porta_webdriver = 0
        validacao_porta = None
        while validacao_porta is not False:
            limite_porta_minima = 49152
            limite_porta_maxima = 65535
            porta_webdriver = randint(limite_porta_minima, limite_porta_maxima)
            validacao_porta = validar_porta('localhost', porta_webdriver)
    else:
        if isinstance(porta_webdriver, int) is False:
            raise ValueError(
                'Parâmetro ``porta_webdriver`` precisa ser número e do tipo inteiro.'
            )

    def retorna_service(executavel_webdriver, nome_navegador, porta_webdriver):
        if nome_navegador.upper().__contains__('CHROME'):
            from selenium.webdriver.chrome.service import Service
        if nome_navegador.upper().__contains__('EDGE'):
            from selenium.webdriver.edge.service import Service
        if nome_navegador.upper().__contains__('FIREFOX'):
            from selenium.webdriver.firefox.service import Service

        executavel = python_utils.coletar_caminho_absoluto(executavel_webdriver)

        service = Service(executable_path=executavel, port=porta_webdriver)
        return service

    def adicionar_extras(
        options_webdriver,
        argumento,
        extensao,
        argumento_experimental,
        capacidade,
    ):
        if len(argumento) > 0:
            for item in argumento:
                options_webdriver.add_argument(item)

        if len(extensao) > 0:
            for item in extensao:
                options_webdriver.add_extension(item)

        if len(argumento_experimental) > 0:
            for item in argumento_experimental:
                options_webdriver.add_experimental_option(*item)

        if len(capacidade) > 0:
            for item in capacidade:
                options_webdriver.set_capability(item[0], item[1])
            options_webdriver.to_capabilities()

        return options_webdriver

    if baixar_webdriver_previamente is True:
        (
            url_webdriver,
            caminho_arquivo_zip,
            informacao_webdriver,
        ) = _preparar_ambiente(nome_navegador)

        executavel_webdriver = str('/').join(
            (
                informacao_webdriver.caminho,
                informacao_webdriver.nome_arquivo,
            )
        )

        executavel_webdriver = python_utils.coletar_caminho_absoluto(
            executavel_webdriver
        )

        if not python_utils.caminho_existente(executavel_webdriver):
            validacao_baixar_arquivo = baixar_arquivo(
                url_webdriver,
                caminho_arquivo_zip,
            )

            validacao_caminho_arquivo_zip = 0
            while not (
                validacao_caminho_arquivo_zip == informacao_webdriver.tamanho
            ):
                validacao_caminho_arquivo_zip = str(
                    _coletar_tamanho(caminho_arquivo_zip)
                )

            caminho_descompactar = python_utils.coletar_caminho_absoluto(
                informacao_webdriver.caminho
            )

            python_utils.descompactar(
                arquivo=caminho_arquivo_zip,
                caminho_destino=caminho_descompactar,
            )
        else:
            executavel_webdriver = str(executavel_webdriver)
    else:
        if executavel == 'padrao':
            raise SystemError('Informe o executável do webdriver.')
        else:
            if not executavel.__contains__('.exe'):
                raise SystemError('Informe o executável do webdriver.')
            else:
                executavel_webdriver = python_utils.coletar_caminho_absoluto(
                    executavel
                )

    if nome_navegador.upper().__contains__('CHROME'):
        options_webdriver = webdriver.ChromeOptions()
        instancia_webdriver = webdriver.Chrome
    elif nome_navegador.upper().__contains__('EDGE'):
        options_webdriver = webdriver.EdgeOptions()
        instancia_webdriver = webdriver.Edge
    elif nome_navegador.upper().__contains__('FIREFOX'):
        options_webdriver = webdriver.FirefoxOptions()
        instancia_webdriver = webdriver.Firefox
    else:
        raise SystemError(
            f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
        )

    options_webdriver = adicionar_extras(
        options_webdriver=options_webdriver,
        argumento=options,
        extensao=extensoes,
        argumento_experimental=experimentos,
        capacidade=capacidades,
    )

    _navegador = instancia_webdriver(
        service=retorna_service(
            executavel_webdriver,
            nome_navegador,
            porta_webdriver,
        ),
        options=options_webdriver,
    )

    abrir_pagina(url)

    return True


def autenticar_navegador(
    nome_navegador: str,
    titulo_janela: str,
    usuario: str,
    senha: str,
) -> bool:
    from time import sleep

    lista_processos_navegadores = (
        'EDGE',
        'CHROME',
        'FIREFOX',
    )

    if not nome_navegador.upper() in lista_processos_navegadores:
        raise NameError(
            'Escolha um desses nomes de navegador: Edge, Chrome, Firefox.'
        )

    nome_janela_navegador = ''
    pid_janela_credenciais = python_utils.coletar_pid(nome_navegador)
    lista_relacao_janelas = []
    pid_janela_navegador = 0
    nome_janela_navegador = ''
    for indice_lista_janela in range(0, len(pid_janela_credenciais)):
        try:
            pid = pid_janela_credenciais[indice_lista_janela]['pid']
            desktop_utils.conectar_app(
                pid, estilo_aplicacao='uia', tempo_espera=1
            )
            lista_relacao_janelas.append(
                [pid, desktop_utils.retornar_janelas_disponiveis(pid)]
            )
        except:
            pass

    for janela in range(0, len(lista_relacao_janelas)):
        if not lista_relacao_janelas[janela][1] == []:
            pid_janela_navegador = lista_relacao_janelas[janela][0]
            nome_janela_navegador = lista_relacao_janelas[janela][1][0]
            if nome_janela_navegador.__contains__(titulo_janela):
                break

    desktop_utils.conectar_app(pid_janela_navegador)
    desktop_utils.ativar_foco(nome_janela_navegador)

    desktop_utils.simular_digitacao(usuario)
    desktop_utils.simular_digitacao('{TAB}')
    desktop_utils.simular_digitacao(senha)
    desktop_utils.simular_digitacao('{TAB}')
    desktop_utils.simular_digitacao('{ENTER}')

    return True


def abrir_pagina(url: str):
    """Abre uma página web mediante a URL informada."""
    global _navegador

    _navegador.get(url)
    esperar_pagina_carregar()


def abrir_janela(url: str = None):
    """Abre uma nova janela/aba do navegador automatizado."""
    _navegador.window_handles
    _navegador.execute_script(f'window.open("{url}")')


def trocar_para(id, tipo):
    """Troca de contexto da automação web mediante o tipo e o id informados."""

    try:
        resultado = True
        if tipo.upper() == 'FRAME':
            _navegador.switch_to.frame(id)
        elif tipo.upper() == 'PARENT_FRAME':
            _navegador.switch_to.parent_frame(id)
        elif tipo.upper() == 'NEW_WINDOW':
            _navegador.switch_to.new_window(id)
        elif tipo.upper() == 'WINDOW':
            _navegador.switch_to.window(id)
        elif tipo.upper() == 'ALERT':
            if id.upper() == 'TEXT':
                resultado = _navegador.switch_to.alert.text
            elif id.upper() == 'DISMISS':
                _navegador.switch_to.alert.dismiss()
            elif id.upper() == 'ACCEPT':
                _navegador.switch_to.alert.accept()
            elif id.upper().__contains__('SEND_KEYS'):
                metodo, valor = id
                _navegador.switch_to.alert.send_keys(valor)
            else:
                _navegador.switch_to.alert.accept()
        elif tipo.upper() == 'ACTIVE_ELEMENT':
            _navegador.switch_to.active_element(id)
        elif tipo.upper() == 'DEFAULT_CONTENT':
            _navegador.switch_to.default_content()
        try:
            esperar_pagina_carregar()
        except:
            ...
        return resultado
    except:
        return False


def coletar_id_janela():
    """Coleta um ID de uma janela/aba."""
    id_janela = _navegador.current_window_handle

    return id_janela


def coletar_todas_ids_janelas():
    """Coleta uma lista de todos os ID's de
    janelas/abas do navegador automatizado."""
    ids_janelas = _navegador.window_handles

    return ids_janelas


def esperar_pagina_carregar():
    """Espera o carregamento total da página automatizada acontecer."""

    estado_pronto = False
    while estado_pronto is False:
        state = _navegador.execute_script('return window.document.readyState')

        if state == 'complete':
            estado_pronto = True


def voltar_pagina():
    """Volta o contexto de histórico do navegador automatizado."""
    _navegador.back()

    esperar_pagina_carregar()


def centralizar_elemento(seletor, tipo_elemento='CSS_SELECTOR'):
    """Centraliza um elemento informado na tela."""
    seletor = seletor.replace('"', "'")

    if tipo_elemento.upper() == 'CSS_SELECTOR':
        _navegador.execute_script(
            'document.querySelector("'
            + seletor
            + "\").scrollIntoView({block:  'center'})"
        )
    elif tipo_elemento.upper() == 'XPATH':
        _navegador.execute_script(
            'elemento = document.evaluate("'
            + seletor
            + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)\
            .singleNodeValue; elemento.scrollIntoView({block: 'center'});"
        )


def executar_script(script, args=''):
    """Executa um script Javascript na página automatizada."""
    try:
        if not args == '':
            _navegador.execute_script(script, args)
        else:
            _navegador.execute_script(script)

        return True
    except:
        return False


def retornar_codigo_fonte():
    """Coleta e retorna o código HTML da página automatizada."""
    codigo_fonte = _navegador.page_source

    return codigo_fonte


def aguardar_elemento(
    identificador: str or int,
    tipo_elemento: str = 'CSS_SELECTOR',
    valor: str or tuple or bool = '',
    comportamento_esperado: str = 'VISIBILITY_OF_ELEMENT_LOCATED',
    tempo: int = 30,
):
    """Aguarda o elemento informado estar visível na tela."""
    from selenium.webdriver.support.ui import WebDriverWait

    _lista_ec_sem_parametro = ['ALERT_IS_PRESENT']
    _lista_ec_com_locator = [
        'ELEMENT_LOCATED_TO_BE_SELECTED',
        'FRAME_TO_BE_AVAILABLE_AND_SWITCH_TO_IT',
        'INVISIBILITY_OF_ELEMENT_LOCATED',
        'PRESENCE_OF_ALL_ELEMENTS_LOCATED',
        'PRESENCE_OF_ELEMENT_LOCATED',
        'VISIBILITY_OF_ALL_ELEMENTS_LOCATED',
        'VISIBILITY_OF_ANY_ELEMENTS_LOCATED',
        'VISIBILITY_OF_ELEMENT_LOCATED',
        'ELEMENT_TO_BE_CLICKABLE',
    ]
    _lista_ec_com_locator_texto = [
        'TEXT_TO_BE_PRESENT_IN_ELEMENT',
        'TEXT_TO_BE_PRESENT_IN_ELEMENT_VALUE',
    ]
    _lista_ec_com_locator_boleano = ['ELEMENT_LOCATED_SELECTION_STATE_TO_BE']
    _lista_ec_com_element_boleano = ['ELEMENT_SELECTION_STATE_TO_BE']
    _lista_ec_com_locator_atributo = ['ELEMENT_ATTRIBUTE_TO_INCLUDE']
    _lista_ec_com_locator_atributo_texto = [
        'TEXT_TO_BE_PRESENT_IN_ELEMENT_ATTRIBUTE'
    ]
    _lista_ec_com_titulo = ['TITLE_CONTAINS', 'TITLE_IS']
    _lista_ec_com_url = ['URL_CHANGES', 'URL_CONTAINS', 'URL_TO_BE']
    _lista_ec_com_pattern = ['URL_MATCHES']
    _lista_ec_com_element = [
        'ELEMENT_TO_BE_SELECTED',
        'INVISIBILITY_OF_ELEMENT',
        'STALENESS_OF',
        'VISIBILITY_OF',
    ]
    _lista_ec_com_ec = ['ALL_OF', 'ANY_OF', 'NONE_OF']
    _lista_ec_com_handle = ['NEW_WINDOW_IS_OPENED']
    _lista_ec_com_int = ['NUMBER_OF_WINDOWS_TO_BE']

    try:
        wait = WebDriverWait(_navegador, tempo)

        tipo_elemento_escolhido = _escolher_tipo_elemento(tipo_elemento)
        tipo_comportamento_esperado = _escolher_comportamento_esperado(
            comportamento_esperado
        )
        complemento = False

        if (identificador == '') and (tipo_elemento == ''):
            if comportamento_esperado in _lista_ec_sem_parametro:
                wait.until(tipo_comportamento_esperado())
            elif comportamento_esperado in _lista_ec_com_handle:
                wait.until(
                    tipo_comportamento_esperado(_navegador.window_handles)
                )
        elif (
            (identificador == '')
            or (tipo_elemento == '')
            or (comportamento_esperado in _lista_ec_com_ec)
        ):
            raise
        else:
            if (comportamento_esperado in _lista_ec_com_locator) or (
                comportamento_esperado in _lista_ec_com_element
            ):
                wait.until(
                    tipo_comportamento_esperado(
                        (tipo_elemento_escolhido, identificador)
                    )
                )
                complemento = True
            elif (
                (comportamento_esperado in _lista_ec_com_locator_texto)
                or (comportamento_esperado in _lista_ec_com_locator_atributo)
                or (comportamento_esperado in _lista_ec_com_locator_boleano)
            ):
                wait.until(
                    tipo_comportamento_esperado(
                        (tipo_elemento_escolhido, identificador), valor
                    )
                )
                complemento = True
            elif comportamento_esperado in _lista_ec_com_element_boleano:
                wait.until(
                    tipo_comportamento_esperado(
                        _procurar_elemento(
                            tipo_elemento_escolhido, identificador
                        ),
                        valor,
                    )
                )
                complemento = True
            elif (
                comportamento_esperado in _lista_ec_com_locator_atributo_texto
            ):
                atributo = valor[0]
                texto = valor[1]
                wait.until(
                    tipo_comportamento_esperado(
                        (tipo_elemento_escolhido, identificador),
                        atributo,
                        texto,
                    )
                )
                complemento = True
            elif (
                (comportamento_esperado in _lista_ec_com_titulo)
                or (comportamento_esperado in _lista_ec_com_url)
                or (comportamento_esperado in _lista_ec_com_pattern)
                or (comportamento_esperado in _lista_ec_com_int)
            ):
                wait.until(tipo_comportamento_esperado(identificador))
            else:
                raise

        if complemento is True:
            centralizar_elemento(identificador, tipo_elemento)
            esperar_pagina_carregar()

        return True
    except:
        return False


def procurar_muitos_elementos(seletor, tipo_elemento='CSS_SELECTOR'):
    """Procura todos os elementos presentes que correspondam ao informado."""
    # instancia uma lista vazia
    lista_webelementos_str = []

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    lista_webelementos = _navegador.find_elements(tipo_elemento, seletor)
    centralizar_elemento(seletor, tipo_elemento)

    # para cada elemento na lista de webelementos
    for webelemento in lista_webelementos:
        # coleta e salva o texto do elemento
        lista_webelementos_str.append(webelemento.text)

    # retorna os valores coletados ou uma lista vazia
    return lista_webelementos_str


def procurar_elemento(seletor, tipo_elemento='CSS_SELECTOR'):
    """Procura um elemento presente que corresponda ao informado."""
    try:
        tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
        _navegador.find_element(tipo_elemento, seletor)
        centralizar_elemento(seletor, tipo_elemento)

        return True
    except Exception:
        return False


def selecionar_elemento(
    seletor: str,
    valor: str,
    tipo_elemento: str = 'CSS_SELECTOR',
):
    """Seleciona em elemento de seleção um
    valor que corresponda ao informado."""
    from selenium.webdriver.support.ui import Select

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    aguardar_elemento(seletor, tipo_elemento)

    webelemento = _procurar_elemento(
        seletor,
        tipo_elemento,
    )

    Select(webelemento).select_by_visible_text(valor)

    return True


def contar_elementos(seletor, tipo_elemento='CSS_SELECTOR'):
    """Conta todos os elementos presentes que correspondam ao informado."""
    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    centralizar_elemento(seletor, tipo_elemento)
    elementos = _procurar_muitos_elementos(seletor, tipo_elemento)

    return len(elementos)


def extrair_texto(seletor, tipo_elemento='CSS_SELECTOR'):
    """Extrai o texto de um elemento informado."""
    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    elemento = _procurar_elemento(seletor, tipo_elemento)
    text_element = elemento.text
    centralizar_elemento(seletor, tipo_elemento)

    return text_element


def coletar_atributo(seletor, atributo, tipo_elemento='CSS_SELECTOR'):
    """Coleta o valor de um atributo solicitado do elemento informado."""
    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    elemento = _procurar_elemento(seletor, tipo_elemento)
    centralizar_elemento(seletor, tipo_elemento)
    valor_atributo = elemento.get_attribute(atributo)

    return valor_atributo


def alterar_atributo(
    seletor,
    atributo,
    novo_valor,
    tipo_elemento='CSS_SELECTOR',
):
    """Coleta o valor de um atributo solicitado do elemento informado."""
    seletor = seletor.replace('"', "'")
    tipo_elemento_transformado = _escolher_tipo_elemento(tipo_elemento)
    elemento = _procurar_elemento(seletor, tipo_elemento_transformado)
    centralizar_elemento(seletor, tipo_elemento_transformado)

    if tipo_elemento.upper() == 'XPATH':
        _navegador.execute_script(
            f"""elemento_xpath = document.evaluate(\"{seletor}\",
            document, null, XPathResult.FIRST_ORDERED_NODE_TYPE,
            null).singleNodeValue;elemento.{atributo} = \"{novo_valor}\""""
        )
    elif tipo_elemento.upper() == 'CSS_SELECTOR':
        _navegador.execute_script(
            f"""elemento = document.querySelector(\"{seletor}\");
            elemento.{atributo} = \"{novo_valor}\""""
        )

    valor_atributo = elemento.get_attribute(atributo)

    return valor_atributo


def clicar_elemento(seletor, tipo_elemento='CSS_SELECTOR'):
    """Clica em um elemento informado."""
    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    centralizar_elemento(seletor, tipo_elemento)

    elemento = _procurar_elemento(seletor, tipo_elemento)
    elemento.click()
    esperar_pagina_carregar()


def escrever_em_elemento(
    seletor, texto, tipo_elemento='CSS_SELECTOR', performar: bool = False
):
    """Digita dentro de um elemento informado."""
    from selenium.webdriver import ActionChains

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)

    try:
        centralizar_elemento(seletor, tipo_elemento)
    except:
        ...

    webelemento = _procurar_elemento(seletor, tipo_elemento=tipo_elemento)

    if performar is False:
        webelemento.send_keys(texto)
    else:
        action = ActionChains(_navegador)
        action.click(webelemento).perform()
        webelemento.clear()
        action.send_keys_to_element(webelemento, texto).perform()

    esperar_pagina_carregar()


def limpar_campo(
    seletor, tipo_elemento='CSS_SELECTOR', performar: bool = False
):
    """Digita dentro de um elemento informado."""
    from selenium.webdriver import ActionChains

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    centralizar_elemento(seletor, tipo_elemento)

    webelemento = _procurar_elemento(seletor, tipo_elemento=tipo_elemento)
    if performar is False:
        webelemento.clear()
    else:
        action = ActionChains(_navegador)
        action.click(webelemento).perform()
        webelemento.clear()
        action.send_keys_to_element(webelemento, '').perform()
        action.reset_actions()

    esperar_pagina_carregar()


def performar(acao, seletor, tipo_elemento='CSS_SELECTOR'):
    """Simula uma ação real de mouse."""
    from selenium.webdriver import ActionChains

    action = ActionChains(_navegador)
    webelemento = _procurar_elemento(seletor, tipo_elemento)

    if acao.upper() == 'CLICK':
        action.click(webelemento).perform()
    elif acao.upper() == 'DOUBLE_CLICK':
        action.double_click(webelemento).perform()
        action = ActionChains(_navegador)
    elif acao.upper() == 'MOVE_TO_ELEMENT':
        action.move_to_element(webelemento).perform()

    return True


def print_para_pdf(
    caminho_arquivo: str,
    escala: float = 1.0,
    paginacao: list[str] = None,
    fundo: bool = None,
    encolher_para_caber: bool = None,
    orientacao: int = None,
):
    """Realiza o print da página atual e salva em um arquivo informado."""
    # importa recursos do módulo base64
    import base64

    # importa recursos do módulo print_page_options
    from selenium.webdriver.common.print_page_options import PrintOptions

    try:
        # coleta o caminho completo do arquivo informado
        caminho_arquivo_absoluto = python_utils.coletar_caminho_absoluto(
            caminho_arquivo
        )

        # Instancia o objeto de print
        opcoes_print = PrintOptions()

        # caso os parâmetros não sejam None:
        if escala is not None:
            # define a escala
            opcoes_print.scale = escala
        if paginacao is not None:
            # define a paginação
            opcoes_print.page_ranges = paginacao
        if fundo is not None:
            # define o fundo
            opcoes_print.background = fundo
        if encolher_para_caber is not None:
            # define o ajuste de tamanho da página
            opcoes_print.shrink_to_fit = encolher_para_caber
        if orientacao is not None:
            # define a orientação da página
            orientacao_escolhida = opcoes_print.ORIENTATION_VALUES[orientacao]
            opcoes_print.orientation = orientacao_escolhida

        # coleta o hash base64 do print
        cache_base_64 = _navegador.print_page(opcoes_print)

        # inicia o gerenciador de contexto no arquivo de saída
        with open(caminho_arquivo_absoluto, 'wb') as arquivo_saida:
            # grava o hash base64 no arquivo de saida
            arquivo_saida.write(base64.b64decode(cache_base_64))

        # retorna True em caso de sucesso
        return True
    except:
        # retorna False em caso de falha
        return False


def fechar_janela(janela):
    """Fecha uma janela/aba do navegador automatizado."""
    _navegador.switch_to.window(janela)
    _navegador.close()


def fechar_janelas_menos_essa(id_janela):
    """Fecha todas as janelas/abas do
    navegador automatizado menos a informada."""
    lista_janelas = _navegador.window_handles
    for janela in lista_janelas:
        if janela != id_janela:
            _navegador.switch_to.window(janela)
            _navegador.close()


def encerrar_navegador():
    """Fecha a instância do navegador automatizado."""
    try:
        for janela in _navegador.window_handles:
            fechar_janela(janela)
        else:
            _navegador.quit()

        return True
    except:
        return False
