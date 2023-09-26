"""Módulo para automação web."""
from py_rpautom import desktop_utils as desktop_utils
from py_rpautom import python_utils as python_utils


__all__ = [
    'abrir_janela',
    'abrir_pagina',
    'atualizar_pagina',
    'aguardar_elemento',
    'alterar_atributo',
    'autenticar_navegador',
    'baixar_arquivo',
    'centralizar_elemento',
    'clicar_elemento',
    'coletar_atributo',
    'coletar_id_janela',
    'coletar_todas_ids_janelas',
    'contar_elementos',
    'encerrar_navegador',
    'escrever_em_elemento',
    'esperar_pagina_carregar',
    'executar_script',
    'extrair_texto',
    'fechar_janela',
    'fechar_janelas_menos_essa',
    'iniciar_navegador',
    'limpar_campo',
    'performar',
    'print_para_pdf',
    'procurar_elemento',
    'procurar_muitos_elementos',
    'requisitar_url',
    'retornar_codigo_fonte',
    'selecionar_elemento',
    'trocar_para',
    'validar_porta',
    'voltar_pagina',
]


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
    stream: bool = True,
    verificacao_ssl: bool = True,
    autenticacao: None or list = None,
    header_arg: str = None,
    tempo_limite: int or float = 1,
    proxies : dict[str, str] = None,
):
    """Faz uma requisição http, retornando a resposta
    dessa requisição no padrão http/https."""
    from os import environ
    from requests import get
    from requests.auth import HTTPBasicAuth

    if autenticacao is not None:
        usuario, senha = autenticacao
        autenticacao = HTTPBasicAuth(usuario, senha)

    resposta = get(
        url=url,
        stream=stream,
        verify=verificacao_ssl,
        auth=autenticacao,
        headers=header_arg,
        timeout=tempo_limite,
        proxies=proxies,
    )

    return resposta


def baixar_arquivo(
    url,
    caminho_destino,
    stream=True,
    verificacao_ssl: bool = True,
    autenticacao: None or list = None,
    header_arg=None,
    tempo_limite: int or float = 1,
    proxies : dict[str, str] = None,
) -> bool:
    """Baixa um arquivo mediante uma url do arquivo e um
    caminho de destino já com o nome do arquivo a ser gravado."""
    from shutil import copyfileobj

    caminho_interno_absoluto = python_utils.coletar_caminho_absoluto(
        caminho_destino
    )

    resposta = requisitar_url(
        url = url,
        stream = stream,
        verificacao_ssl = verificacao_ssl,
        autenticacao = autenticacao,
        header_arg = header_arg,
        tempo_limite = tempo_limite,
        proxies=proxies,
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
    options: tuple[tuple[str]] = None,
    extensoes: tuple[tuple[str]] = None,
    experimentos: tuple[tuple[str, str]] = None,
    capacidades: tuple[tuple[str, str]] = None,
    executavel: str = None,
    caminho_navegador: str = None,
    porta_webdriver: int = None,
    proxies : dict[str, str] = None,
    baixar_webdriver_previamente: bool = True,
):
    """Inicia uma instância automatizada de um navegador."""
    from collections import namedtuple
    from urllib3 import disable_warnings

    global _navegador
    global _service
    global wdm_ssl_verify

    disable_warnings()
    wdm_ssl_verify = python_utils.ler_variavel_ambiente(
        nome_variavel='WDM_SSL_VERIFY',
        variavel_sistema = True,
    )

    webdriver_info = namedtuple(
        'webdriver_info',
        [
            'nome',
            'caminho',
            'plataforma',
            'versao',
            'nome_arquivo',
            'tamanho',
        ],
    )
    
    webdriver_info.nome = None
    webdriver_info.caminho = None
    webdriver_info.plataforma = None
    webdriver_info.versao = None
    webdriver_info.nome_arquivo = None
    webdriver_info.tamanho = None

    if nome_navegador.upper().__contains__('CHROME'):
        if caminho_navegador is None:
            caminho_navegador = (
                'C:/Program Files/Google/Chrome/Application/chrome.exe'
            )
        webdriver_info.nome = 'chromedriver'
        url_base = 'https://chromedriver.storage.googleapis.com'
    elif nome_navegador.upper().__contains__('EDGE'):
        if caminho_navegador is None:
            caminho_navegador = (
                'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
            )
        webdriver_info.nome = 'edgedriver'
        url_base = 'https://msedgedriver.azureedge.net'
    elif nome_navegador.upper().__contains__('FIREFOX'):
        if caminho_navegador is None:
            caminho_navegador = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        webdriver_info.nome = 'geckodriver'
        url_base = 'https://github.com/mdn/content/blob/main/files/en-us/glossary/gecko/index.md?plain=1'
    else:
        raise SystemError(
            f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
        )


    def _coletar_versao_webdriver(executavel_webdriver):
        import subprocess

        execucao_webdriver = subprocess.Popen(
            [executavel_webdriver, '-V'], stdout=subprocess.PIPE
        )

        versao_webdriver = str(execucao_webdriver.stdout.read())
        versao_webdriver = versao_webdriver.partition(' (')[0]
        versao_webdriver = versao_webdriver.rpartition(' ')[-1]

        return versao_webdriver


    def _retornar_service(
        executavel_webdriver,
        nome_navegador,
        porta_webdriver,
    ):
        if nome_navegador.upper().__contains__('CHROME'):
            from selenium.webdriver.chrome.service import Service
        elif nome_navegador.upper().__contains__('EDGE'):
            from selenium.webdriver.edge.service import Service
        elif nome_navegador.upper().__contains__('FIREFOX'):
            from selenium.webdriver.firefox.service import Service
        else:
            raise SystemError(
                f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
            )

        executavel = python_utils.coletar_caminho_absoluto(executavel_webdriver)

        service = Service(executable_path=executavel, port=porta_webdriver,)

        return service


    def _retornar_webdriver_options(nome_navegador):
        from selenium import webdriver

        if nome_navegador.upper().__contains__('CHROME'):
            options_webdriver = webdriver.ChromeOptions()
        elif nome_navegador.upper().__contains__('EDGE'):
            options_webdriver = webdriver.EdgeOptions()
        elif nome_navegador.upper().__contains__('FIREFOX'):
            options_webdriver = webdriver.FirefoxOptions()
        else:
            raise SystemError(
                f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
            )

        return options_webdriver


    def _instanciar_webdriver(
        service,
        webdriver_options = None,
    ):
        from selenium.webdriver import Remote

        service.start()

        _navegador = Remote(
            command_executor=service.service_url,
            options=webdriver_options,
            keep_alive=True,
        )

        _navegador.get(url)

        return _navegador


    def _adicionar_extras(
        options_webdriver,
        argumento,
        extensao,
        argumento_experimental,
        capacidade,
    ):
        if argumento is not None and len(argumento) > 0:
            for item in argumento:
                options_webdriver.add_argument(item)

        if extensao is not None and len(extensao) > 0:
            for item in extensao:
                options_webdriver.add_extension(item)

        if argumento_experimental is not None and len(argumento_experimental) > 0:
            for item in argumento_experimental:
                options_webdriver.add_experimental_option(*item)

        if capacidade is not None and len(capacidade) > 0:
            for item in capacidade:
                options_webdriver.set_capability(item[0], item[1])
            options_webdriver.to_capabilities()

        return options_webdriver


    def _criar_pasta_webdriver(
        webdriver_info: webdriver_info,
    ):
        from pathlib import Path

        caminho_usuario = Path.home()
        caminho_webdriver_raiz = 'webdrivers'

        webdriver_info.caminho = str(
            caminho_usuario /
            caminho_webdriver_raiz /
            webdriver_info.nome
        )

        # caso o caminho existir
        if not python_utils.caminho_existente(webdriver_info.caminho):
            # cria a pasta informada, caso necessário
            #  cria a hierarquia anterior à última pasta
            python_utils.criar_pasta(webdriver_info.caminho)

        return webdriver_info


    def _coletar_lista_webdrivers(
        url: str,
        nome_navegador: str,
        webdriver_info: webdriver_info,
        header_arg: None,
        proxies : dict[str, str] = None,
    ):
        from os import environ
        from requests.exceptions import SSLError

        global wdm_ssl_verify

        status = 0
        contagem = 0
        
        resposta = None
        if wdm_ssl_verify is None:
            environ['WDM_SSL_VERIFY'] = '1'
            wdm_ssl_verify = '1'

        while not status == 200 and contagem < 60:
            verificacao_ssl = (
                environ['WDM_SSL_VERIFY']
            ).lower() in ['1', 1, 'true', True,]

            try:
                resposta = requisitar_url(
                    url,
                    stream=True,
                    verificacao_ssl = verificacao_ssl,
                    autenticacao=['', ''],
                    header_arg=header_arg,
                    tempo_limite = 1,
                )
                status = resposta.status_code

                if status in range(200, 300):
                    break
                else:
                    resposta = requisitar_url(
                        url,
                        stream=True,
                        verificacao_ssl = verificacao_ssl,
                        header_arg=header_arg,
                        tempo_limite = 1,
                    )
                    status = resposta.status_code
            except SSLError as erro:
                environ['WDM_SSL_VERIFY'] = '0'
                wdm_ssl_verify = '0'
            except Exception as erro:
                ...

            contagem = contagem + 1

        if not resposta.status_code in range(200, 300):
            raise SystemError(
                f'Falha ao acessar a url {url}. Revise os dados e tente novamente.'
            )

        return resposta


    def _tratar_lista_webdrivers(response_http_webdrivers):
        from xml.etree.ElementTree import fromstring

        root = fromstring(response_http_webdrivers.content)

        if nome_navegador.upper().__contains__('CHROME'):
            inicio_url = root.tag.index('{') + 1 or 0
            final_url = root.tag.index('}') or 0
            endereco_url_elemento_xml = (
                root.tag[inicio_url:final_url] or ''
            )
            tag_nome_webdriver = (
                '*//{' + endereco_url_elemento_xml + '}Key'
            )
            tag_url_webdriver = None
            tag_tamanho_webdriver = (
                '*//{' + endereco_url_elemento_xml + '}Size'
            )
        elif nome_navegador.upper().__contains__('EDGE'):
            tag_nome_webdriver = '*//Name'
            tag_url_webdriver = '*//Url'
            tag_tamanho_webdriver = '*//Content-Length'
        elif nome_navegador.upper().__contains__('FIREFOX'):
            tag_nome_webdriver = ''
            tag_url_webdriver = None
            tag_tamanho_webdriver = None
        else:
            raise SystemError(
                f' {nome_navegador} não disponível. Escolha uma dessas opções: Chrome, Edge, Firefox.'
            )


        lista_nome_webdrivers = [
            item.text
            for item in root.findall(tag_nome_webdriver)
        ]        

        if tag_url_webdriver is None:
            lista_url_webdrivers = [
                None for item in range(len(lista_nome_webdrivers))
            ]
        else:
            lista_url_webdrivers = [
                item.text
                for item in root.findall(tag_url_webdriver)
            ]

        if tag_tamanho_webdriver is None:
            lista_tamanho_webdrivers = [
                None for item in range(len(lista_nome_webdrivers))
            ]
        else:
            lista_tamanho_webdrivers = [
                item.text
                for item in root.findall(tag_tamanho_webdriver)
            ]
            

        lista_webdrivers = list(
            zip(
                lista_nome_webdrivers,
                lista_url_webdrivers,
                lista_tamanho_webdrivers,
            )
        )

        return lista_webdrivers


    if porta_webdriver is not None:
        if isinstance(porta_webdriver, int) is False:
            raise ValueError(
                'Parâmetro ``porta_webdriver`` precisa ser número e do tipo inteiro.'
            )

    versao_navegador = None
    versao_webdriver = None
    if baixar_webdriver_previamente is True:
        webdriver_info = _criar_pasta_webdriver(
            webdriver_info = webdriver_info,
        )

        versao_sistema = python_utils.coletar_versao_so()
        divisao_pastas = '/'
        if versao_sistema == 'win32':
            webdriver_info.plataforma = 'win32'
            divisao_pastas = '\\'
        elif versao_sistema == 'linux' or versao_sistema == 'linux2':
            webdriver_info.plataforma = 'linux32'
        elif versao_sistema == 'darwin':
            webdriver_info.plataforma = 'mac64'
        else:
            ValueError('Sistema não suportado, utilize Windows, Linux ou MacOS.')

        versao_navegador = (
            python_utils.coletar_versao_arquivo(caminho_navegador)
        )
        versao_navegador_sem_minor = '.'.join(
            [
                str(parte_versao)
                for parte_versao in map(int, versao_navegador)
            ][:-1]
        )

        lista_webdrivers_locais = python_utils.retornar_arquivos_em_pasta(
            caminho=webdriver_info.caminho,
            filtro=f'{versao_navegador_sem_minor}*'
        )

        validacao_download = None
        if len(lista_webdrivers_locais) == 0:
            versao_webdriver_local_sem_minor = ''
            validacao_download = True
        else:
            lista_webdrivers_locais.sort()
            webdriver_local = lista_webdrivers_locais[-1]
            versao_webdriver_local = (
                webdriver_local.rpartition(divisao_pastas)[-1]
            )
            versao_webdriver_local_separado = (
                versao_webdriver_local.split('.')
            )
            versao_webdriver_local_sem_minor = '.'.join(
                versao_webdriver_local_separado[:-1]
            )

        webdriver_info.versao = versao_navegador_sem_minor
        if versao_navegador_sem_minor == versao_webdriver_local_sem_minor:
            caminho_base_webdriver = divisao_pastas.join(
                (
                    webdriver_info.caminho,
                    versao_webdriver_local,
                )
            )
            executavel = python_utils.retornar_arquivos_em_pasta(
                caminho=caminho_base_webdriver,
                filtro='*.exe',
            )

            if len(executavel) == 0:
                validacao_download = True
            else:
                executavel = executavel[0]
                validacao_download = False
        else:
            validacao_download = True

        if validacao_download is True:
            header_request = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cache-Control': 'max-age=0',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
            }

            response_http_webdrivers = _coletar_lista_webdrivers(
                url = url_base,
                nome_navegador = nome_navegador,
                webdriver_info = webdriver_info,
                header_arg = header_request,
                proxies = proxies,
            )
            lista_webdrivers = _tratar_lista_webdrivers(
                response_http_webdrivers
            )
            if len(lista_webdrivers) == 0:
                raise SystemError(
                    f'Não foi possível coletar as informações do webdriver online, verifique sua conexão de rede.'
                )

            lista_webdrivers_compativeis = []
            for dados_webdriver in lista_webdrivers:
                if (
                    dados_webdriver[0].partition('/')[0]
                    .__contains__(versao_navegador_sem_minor)
                ) \
                and (
                    dados_webdriver[0].partition('/')[-1]
                    .__contains__(webdriver_info.plataforma)
                ):
                    lista_webdrivers_compativeis.append(
                        dados_webdriver
                    )

            if lista_webdrivers_compativeis == []:
                raise SystemError(
                    f'Nenhum webdriver para o navegador {nome_navegador} com a versão {versao_navegador} está disponível no momento.'
                )

            ultimo_webdriver = lista_webdrivers_compativeis[-1]
            webdriver_info.nome_arquivo = (
                ultimo_webdriver[0].partition('/')[-1]
            )
            webdriver_info.versao = (
                ultimo_webdriver[0].partition('/')[0]
            )
            webdriver_info.tamanho = ultimo_webdriver[2]

            url_arquivo_zip = str('/').join(
                (
                    url_base,
                    webdriver_info.versao,
                    webdriver_info.nome_arquivo,
                )
            )

            caminho_arquivo_zip = '\\'.join(
                (
                    webdriver_info.caminho,
                    webdriver_info.versao,
                )
            )

            arquivo_zip = '\\'.join(
                (
                    caminho_arquivo_zip,
                    webdriver_info.nome_arquivo,
                )
            )

            if (
                python_utils.caminho_existente(caminho_arquivo_zip)
                is False
            ):
                python_utils.criar_pasta(
                    caminho = caminho_arquivo_zip
                )

            if wdm_ssl_verify is None:
                wdm_ssl_verify = '1'

            verificacao_ssl = (
                wdm_ssl_verify
            ).lower() in ['1', 1, 'true', True,]

            validacao_arquivo_zip = False
            contagem = 0
            while validacao_arquivo_zip is False and (contagem < 30):
                try:
                    validacao_arquivo_zip = baixar_arquivo(
                        url = url_arquivo_zip,
                        caminho_destino = arquivo_zip,
                        verificacao_ssl = verificacao_ssl,
                        header_arg = header_request,
                        tempo_limite = 1,
                        proxies=proxies,
                    )
                except:
                    ...

                contagem = contagem + 1

            validacao_caminho_arquivo_zip = 0
            contagem = 0
            while not (
                validacao_caminho_arquivo_zip ==
                webdriver_info.tamanho
            ) \
            and (contagem < 30):
                validacao_caminho_arquivo_zip = str(
                    python_utils.coletar_tamanho(arquivo_zip)
                )

            python_utils.descompactar(
                arquivo=arquivo_zip,
                caminho_destino=caminho_arquivo_zip,
            )

            tamanho_executavel = 0
            executavel = python_utils.retornar_arquivos_em_pasta(
                caminho = caminho_arquivo_zip,
                filtro = '*.exe',
            )[0]

            tamanho_executavel = str(
                python_utils.coletar_tamanho(executavel)
            )

    validacao_executavel = None
    if executavel is None:
        validacao_executavel = False
    elif not executavel.endswith('.exe'):
        validacao_executavel = False
    else:
        validacao_executavel = True

    if validacao_executavel is not True:
        if baixar_webdriver_previamente is True:
            raise ValueError('Erro ao validar online o executável do webdriver.')
        else:
            raise ValueError('Informe o executável do webdriver.')

    options_webdriver = _retornar_webdriver_options(
        nome_navegador
    )
    options_webdriver = _adicionar_extras(
        options_webdriver=options_webdriver,
        argumento=options,
        extensao=extensoes,
        argumento_experimental=experimentos,
        capacidade=capacidades,
    )
    _service = _retornar_service(
        executavel,
        nome_navegador,
        porta_webdriver,
    )
    _navegador = _instanciar_webdriver(
        service=_service,
        webdriver_options=options_webdriver,
    )

    abrir_pagina(url)

    return True


def autenticar_navegador(
    usuario: str,
    senha: str,
    caminho_janela: dict,
    caminho_usuario: dict,
    caminho_senha: dict,
    caminho_botao_aprovacao: dict,
    pid_aplicacao: int,
    estilo_aplicacao: str = 'uia',
) -> bool:
    """Autentica em pop-ups de credenciais em navegador.

    Args:
        ``usuario (str)``: String contendo usuário para digitação no campo correspondente.

        ``senha (str)``: String contendo senha para digitação no campo correspondente.

        ``caminho_janela (dict)``: dicionário contendo caminho até o título do navegador.

        ``caminho_usuario (dict)``: dicionário contendo caminho até o elemento usuário no pop-up navegador.

        ``caminho_senha (dict)``: dicionário contendo caminho até o elemento senha no pop-up navegador.

        ``caminho_botao_aprovacao (dict)``: dicionário contendo caminho até o elemento botão de confirmação no pop-up navegador.

        ``pid_aplicacao (int)``: Número inteiro contendo o PID do navegador que contém o popup de autenticação.

        ``estilo_aplicacao (str)``: String contendo o estilo de aplicação entre uia e win32.

    Returns:
        Retorna valor booleano. True for sucesso, False para erro na operação de autenticar.
    """
    #Validar o tipo da varivavel
    if isinstance(usuario, str) is False:
        raise ValueError('``usuario`` precisa ser do tipo str.')

    if isinstance(senha, str) is False:
        raise ValueError('``senha`` precisa ser do tipo str.')

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('``caminho_janela`` precisa ser do tipo dict.')

    if isinstance(caminho_usuario, dict) is False:
        raise ValueError('``caminho_usuario`` precisa ser do tipo dict.')

    if isinstance(caminho_senha, dict) is False:
        raise ValueError('``caminho_senha`` precisa ser do tipo dict.')

    if isinstance(caminho_botao_aprovacao, dict) is False:
        raise ValueError('``caminho_botao_aprovacao`` precisa ser do tipo dict.')

    if isinstance(pid_aplicacao, int) is False:
        raise ValueError('``pid_aplicacao`` precisa ser do tipo int.')

    if isinstance(estilo_aplicacao, str) is False:
        raise ValueError('``estilo_aplicacao`` precisa ser do tipo str.')

    desktop_utils.conectar_app(
        pid_aplicacao,
        estilo_aplicacao = estilo_aplicacao,
        tempo_espera = 1,
    )

    if desktop_utils.localizar_elemento(
        caminho_campo = caminho_janela,
        estilo_aplicacao = estilo_aplicacao,
    ) is True:
        desktop_utils.ativar_foco(nome_janela = caminho_janela)

        desktop_utils.digitar(
            caminho_campo = caminho_usuario,
            valor = usuario,
        )
        desktop_utils.digitar(
            caminho_campo = caminho_senha,
            valor = senha,
        )
        desktop_utils.clicar(
            caminho_campo = caminho_botao_aprovacao,
        )

        return True

    return False


def abrir_pagina(url: str):
    """Abre uma página web mediante a URL informada."""
    global _navegador

    _navegador.get(url)
    esperar_pagina_carregar()


def abrir_janela(url: str = None):
    """Abre uma nova janela/aba do navegador automatizado."""
    _navegador.window_handles
    _navegador.execute_script(f'window.open("{url}")')


def atualizar_pagina():
    """Atualiza a página web."""
    global _navegador

    _navegador.refresh()
    esperar_pagina_carregar()


def trocar_para(id, tipo):
    """Troca de contexto da automação web mediante o tipo e o id informados."""

    try:
        resultado: bool = True
        if tipo.upper() == 'FRAME':
            _navegador.switch_to.frame(id)
        elif tipo.upper() == 'PARENT_FRAME':
            _navegador.switch_to.parent_frame(id)
        elif tipo.upper() == 'NEW_WINDOW':
            _navegador.switch_to.new_window(id)
        elif tipo.upper() == 'WINDOW':
            _navegador.switch_to.window(_navegador.window_handles[id])
        elif tipo.upper() == 'ALERT':
            if id.upper() == 'TEXT':
                resultado: str = _navegador.switch_to.alert.text
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


def coletar_atributo(
    seletor: str,
    atributo: str,
    tipo_elemento: str = 'CSS_SELECTOR',
    metodo: str = 'get_attribute',
):
    """Coleta o valor de um atributo solicitado do elemento informado.
    
    Args:
        ``seletor (str)``: Caminho do seletor HTML (DOM) '
        'correspondente ao tipo de elemento escolhido.

        ``atributo (str)``: Atributo da qual se quer coletar o valor.

        ``tipo_elemento (str)``: Tipo de seletor. '
        'Ex.: xpath, css_selector, link_text...

        ``metodo (str)``: Tipo de coleta. '
        'Ex.: get_attribute, value_of_css_property.

    Returns:
        Retorna o valor coletado."""


    lista_metodos = [
        'get_attribute',
        'get_dom_attribute',
        'value_of_css_property',
    ]

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    elemento = _procurar_elemento(seletor, tipo_elemento)

    centralizar_elemento(seletor, tipo_elemento)

    if metodo.lower() == 'get_attribute':
        valor_atributo = elemento.get_attribute(atributo)
    elif metodo.lower() == 'get_dom_attribute':
        valor_atributo = elemento.get_dom_attribute(atributo)
    elif metodo.lower() == 'value_of_css_property':
        valor_atributo = elemento.value_of_css_property(atributo)
    else:
        raise ValueError(
            f'Escolha entre os seguintes métodos: {lista_metodos}'
        )

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


def clicar_elemento(
    seletor: str,
    tipo_elemento: str = 'CSS_SELECTOR',
    com_alerta: bool = False,
    tempo_alerta: int = 30,
):
    """Clica em um elemento informado."""

    tipo_elemento = _escolher_tipo_elemento(tipo_elemento)
    centralizar_elemento(seletor, tipo_elemento)
    elemento = _procurar_elemento(seletor, tipo_elemento)
    elemento.click()

    if com_alerta is True:
        aguardar_elemento(
            identificador = '',
            tipo_elemento = '',
            comportamento_esperado = 'ALERT_IS_PRESENT',
            tempo = tempo_alerta,
        )

        texto_popup: str = trocar_para(
            id = 'Text',
            tipo = 'ALERT',
        )

        return texto_popup

    esperar_pagina_carregar()

    return True



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
    _navegador.switch_to.window(_navegador.window_handles[janela])
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
        for janela in range(0, len(_navegador.window_handles)):
            fechar_janela(janela)
        else:
            _navegador.quit()

        return True
    except:
        return False
