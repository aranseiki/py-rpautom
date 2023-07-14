"""Módulo para automação de aplicações desktop."""
# importa recursos do módulo pywinauto em nível global
from pywinauto import Application


__all__ = [
    'ativar_foco',
    'capturar_texto',
    'clicar',
    'coletar_arvore_elementos',
    'coletar_dado_selecionado',
    'coletar_dados_selecao',
    'coletar_situacao_janela',
    'conectar_app',
    'digitar',
    'encerrar_app',
    'esta_com_foco',
    'esta_visivel',
    'fechar_janela',
    'iniciar_app',
    'janela_existente',
    'localizar_diretorio_em_treeview',
    'localizar_elemento',
    'maximizar_janela',
    'minimizar_janela',
    'mover_mouse',
    'restaurar_janela',
    'retornar_janelas_disponiveis',
    'selecionar_em_campo_lista',
    'selecionar_em_campo_selecao',
    'selecionar_menu',
    'simular_clique',
    'simular_digitacao',
]


def _aplicacao(estilo_aplicacao: str = 'win32') -> Application:
    """Inicia e retorna um objeto do tipo Application da biblioteca pywinauto."""
    # define app como global
    global APP
    global ESTILO_APLICACAO


    ESTILO_APLICACAO = estilo_aplicacao

    # instancia o objeto application
    APP = Application(backend = ESTILO_APLICACAO)

    # retorna o objeto application instanciado
    return APP


def _conectar_app(
    pid: int,
    tempo_espera: int = 60,
    estilo_aplicacao: str = 'win32',
) -> int:
    """Inicia e retorna um processo do sistema de um
    objeto do tipo Application com o caminho recebido."""
    # define app como global
    global APP
    global ESTILO_APLICACAO


    ESTILO_APLICACAO = estilo_aplicacao

    # instancia o objeto application
    APP = _aplicacao(estilo_aplicacao = ESTILO_APLICACAO)

    # inicia o processo de execução do aplicativo passado como parâmetro
    app_conectado: Application = APP.connect(
        process=pid,
        timeout=tempo_espera,
        backend=estilo_aplicacao,
    )

    # retorna o objeto Application atrelado ao PID informado
    return app_conectado


def _localizar_elemento(
    caminho_campo: dict,
) -> Application:
    """Localiza e retorna um objeto do tipo Application
    percorrendo o caminho até o último o elemento."""
    # importa app para o escopo da função
    global APP

    # inicializa APP para uma variável interna
    app_interno = APP

    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    validacao_fim_dicio = False
    app_mais_interno = app_interno
    while validacao_fim_dicio is False:
        parametros = {
            'title':None,
            'control_type':None,
            'auto_id':None,
            'session':None,
            'child_window':None,
        }

        validacao_janela = False
        if caminho_campo.keys().__contains__('window'):
            caminho_campo = caminho_campo['window']
            validacao_janela = True

        for argumento in (
            'title',
            'control_type',
            'auto_id',
            'session',
            'child_window',
        ):
            if caminho_campo.keys().__contains__(argumento):
                parametros[argumento] = caminho_campo[argumento]

        if validacao_janela is True:
            acao = 'window'
        else:
            acao = 'child_window'

        comando = (
            f'app_mais_interno.{acao}('
                'title=parametros["title"], '
                'auto_id=parametros["auto_id"], '
                'control_type=parametros["control_type"],'
            ')'
        )

        app_mais_interno = eval(comando)

        if parametros['session'] is not None:
            app_mais_interno = app_mais_interno[parametros['session']]

        if parametros['child_window'] is not None:
            caminho_campo = parametros['child_window']
        else:
            validacao_fim_dicio = True

    return app_mais_interno


def ativar_foco(nome_janela: str) -> bool:
    """Ativa a janela de um objeto do tipo Application deixando-a com foco."""
    # importa app para o escopo da função
    global APP

    try:
        # inicializa APP para uma variável interna
        app_interno = APP

        # ativa a janela informada
        app_interno.window(title = nome_janela).set_focus()

        # retorna verdadeiro confirmando a execução da ação
        return True
    except:
        return False


def capturar_texto(caminho_campo: dict) -> str:
    """Captura o texto de um elemento
    dentro de um objeto do tipo Application."""
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # captura o texto do campo localizado
    valor_capturado: str = app_interno.texts()[0]

    # retorna o valor capturado
    return valor_capturado


def clicar(
    caminho_campo: dict, 
    performar: bool = False,
    indice : int = None,
) -> bool:
    """Clica em um elemento dentro de um objeto do tipo Application."""

    # localiza o elemento até o final da árvore de parantesco do app
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    if isinstance(performar, bool) is False:
        raise ValueError('`performar` precisa ser do tipo boleano.')

    if isinstance(indice, int) is False \
    and indice is not None:
        raise ValueError('`indice` precisa ser do tipo int.')

    app_interno = _localizar_elemento(caminho_campo)
    app_interno.exists()

    if indice is not None:
        app_interno = app_interno.children()[indice]

    # digita o valor no campo localizado
    if performar is True:
        app_interno.click_input()
    else:
        app_interno.click()

    # retorna o valor capturado e tratado
    return True


def coletar_arvore_elementos(caminho_elemento: dict) -> list[str]:
    """Lista um elemento dentro de um objeto do
    tipo Application e retorna o valor coletado."""
    # importa recursos do módulo io
    import io
    # importa recursos do módulo Path
    from contextlib import redirect_stdout

    if isinstance(caminho_elemento, dict) is False:
        raise ValueError('`caminho_elemento` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_elemento)

    conteudoStdOut = io.StringIO()
    with redirect_stdout(conteudoStdOut):
        app_interno.print_control_identifiers()

    valor = conteudoStdOut.getvalue()
    valor_dividido = valor.split('\n')

    # retorna o valor capturado e tratado
    return valor_dividido


def coletar_dado_selecionado(caminho_campo: dict) -> str:
    """Coleta dado já selecionado em um elemento
    de seleção em um objeto do tipo Application."""
    # define estático como falso para trabalhar com elemento dinâmico
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # captura o texto do campo localizado
    valor_capturado: str = app_interno.selected_text()

    # retorna o valor capturado
    return valor_capturado


def coletar_dados_selecao(caminho_campo: dict) -> str:
    """Coleta dados disponíveis para seleção em um
    elemento de seleção em um objeto do tipo Application."""
    # define estático como falso para trabalhar com elemento dinâmico
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # captura o texto do campo localizado
    valor_capturado: str = app_interno.item_texts()

    # retorna o valor capturado
    return valor_capturado


def coletar_situacao_janela(caminho_janela: dict) -> str:
    """Coleta a situação do estado atual de uma
    janela de um objeto do tipo Application."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    # inicializa APP para uma variável interna
    app_interno = APP

    situacao = ''
    # coleta a situacao atual da janela
    situacao_temp = _localizar_elemento(caminho_janela).get_show_state()

    # 1 - Normal
    # 2 - Minimizado
    # 3 - Maximizado
    # Caso não encontre as situações normal, ninimizado e
    #   maximizado, define um valor padrão.
    if situacao_temp == 1:
        situacao = 'normal'
    elif situacao_temp == 2:
        situacao = 'minimizado'
    elif situacao_temp == 3:
        situacao = 'maximizado'
    else:
        situacao = 'não identificado'

    # retorna a situação da janela
    return situacao


def conectar_app(
    pid: int,
    tempo_espera: int = 60,
    estilo_aplicacao: str = 'win32',
) -> int:
    """Inicia e retorna um processo do sistema de um
    objeto do tipo Application com o caminho recebido."""
    # define app como global
    global APP
    global ESTILO_APLICACAO


    ESTILO_APLICACAO = estilo_aplicacao

    # instancia o objeto application
    APP = _aplicacao(estilo_aplicacao = ESTILO_APLICACAO)

    # inicia o processo de execução do aplicativo passado como parâmetro
    app_conectado: Application = _conectar_app(
        pid = pid,
        tempo_espera = tempo_espera,
        estilo_aplicacao = ESTILO_APLICACAO,
    )

    # coleta o PID da aplicação instanciada
    processo_app: int = app_conectado.process

    # retorna o PID coletado
    return processo_app


def digitar(
    caminho_campo: dict,
    valor: str,
) -> str:
    """Digita em um elemento dentro de um objeto do tipo Application."""
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # digita o valor no campo localizado
    app_interno.set_edit_text(
        text = valor,
    )

    # trata o valor capturado conforme o tipo do valor de entrada
    valor_retornado = str(capturar_texto(caminho_campo))

    # retorna o valor capturado e tratado
    return valor_retornado


def encerrar_app(
    pid: int,
    forcar: bool = False,
    tempo_espera: int = 60,
) -> bool:
    """Encerra e retorna um processo do sistema de um
    objeto do tipo Application com o caminho recebido."""
    # importa app para o escopo da função
    global APP

    # conecta a aplicação correspondente ao PID informado
    app_interno: Application = _conectar_app(
        pid = pid,
        tempo_espera = tempo_espera,
        estilo_aplicacao = ESTILO_APLICACAO,
    )

    # encerra o aplicativo em execução
    app_interno.kill(soft = not forcar)

    # retorna o objeto application com o processo encerrado
    return True


def esta_com_foco(nome_janela: str) -> bool:
    """Verifica se a janela de um objeto do tipo Application está com foco."""
    # importa app para o escopo da função
    global APP

    # inicializa APP para uma variável interna
    app_interno = APP

    # retorna a situacao atual de foco da janela
    return app_interno.window(title = nome_janela).has_focus()


def esta_visivel(nome_janela: str) -> str:
    """Verifica se a janela de um objeto do tipo Application está visível."""
    # coleta a situação atual da janela
    situacao = coletar_situacao_janela(nome_janela)

    # define visível para situação 'maximizado' ou 'normal'
    if situacao == 'maximizado' or situacao == 'normal':
        situacao = 'visivel'
    # define não visível para situação 'minimizado'
    elif situacao == 'minimizado':
        situacao = 'não visível'
    # Caso não encontre as situações normal, ninimizado e maximizado
    else:
        # define um valor padrão
        situacao = 'não identificado'

    # retorna a situação da janela
    return situacao


def fechar_janela(caminho_janela: dict) -> bool:
    """Encerra uma janela de um objeto do tipo
    Application com o caminho recebido."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    # inicializa APP para uma variável interna
    app_interno = _localizar_elemento(
        caminho_campo = caminho_janela,
    )

    # fecha a janela informada
    app_interno.close()

    # retorna verdadeiro confirmando a execução da ação
    return True


def iniciar_app(
    executavel: str,
    estilo_aplicacao: str ='win32',
    esperar: tuple = (),
    inverter: bool = False,
    ocioso: bool = False,
) -> int:
    """Inicia e retorna um processo do sistema de um
    objeto do tipo Application com o caminho recebido."""
    # define app como global
    global APP
    global ESTILO_APLICACAO


    ESTILO_APLICACAO = estilo_aplicacao

    # instancia o objeto application
    APP = _aplicacao(estilo_aplicacao = ESTILO_APLICACAO)

    # inicia o processo de execução do aplicativo passado como parâmetro
    APP.start(
        cmd_line=executavel,
        wait_for_idle=ocioso,
    )

    esperar_por = tempo_espera = None
    # verifica se foi passado algum parâmetro para esperar, caso não:
    if esperar == ():
        # aguarda a inicialização da aplicação ficar pronta em até 10 segundos
        esperar_por = 'ready'
        tempo_espera = 10
    else:
        esperar_por, tempo_espera = esperar

    if inverter is False:
        # aguarda a inicialização da aplicação ficar na condição informada
        APP.window().wait(
            wait_for=esperar_por,
            timeout=tempo_espera,
            retry_interval=None,
        )
    else:
        # aguarda a inicialização da aplicação não ficar na condição informada
        APP.window().wait_not(
            wait_for_not=esperar_por,
            timeout=tempo_espera,
            retry_interval=None,
        )

    # coleta o PID da aplicação instanciada
    processo_app: int = APP.process

    # retorna o PID coletado
    return processo_app


def janela_existente(pid, nome_janela) -> bool:
    """Verifica se a janela de um objeto do tipo Application está visível."""
    # coleta a situação atual da janela
    lista_janelas = retornar_janelas_disponiveis(pid)

    # verifica se o nome da janela informada corresponde à alguma janela na lista
    for janela in lista_janelas:
        # caso o nome da janela seja o mesmo da janela atual da lista
        if janela == nome_janela:
            # retorna True
            return True

    # retorna False caso nenhuma janela tenha correspondido
    return False


def localizar_diretorio_em_treeview(
    caminho_janela: dict,
    caminho_diretorio: str,
) -> bool:
    """Localiza um diretório, seguindo a árvore de diretórios informada,\
    dentro de um objeto TreeView do tipo Application."""
    try:
        if isinstance(caminho_janela, dict) is False:
            raise ValueError('`caminho_janela` precisa ser do tipo dict.')

        # localiza e armazena o elemento conforme informado
        app_interno = _localizar_elemento(caminho_janela)

        # seleciona o caminho informado na janela do tipo TreeView
        app_interno.TreeView.get_item(caminho_diretorio).click()

        # clica em Ok para confirmar
        app_interno.OK.click()

        # retorna verdadeiro caso processo seja feito com sucesso
        return True
    except:
        return False


def localizar_elemento(
    caminho_campo: dict,
    estilo_aplicacao = 'win32',
) -> bool:
    """Retorna se o caminho de elementos informado existe
    no objeto do tipo Application sendo manipulado."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # inicializa APP para uma variável interna
    app_interno = _localizar_elemento(
        caminho_campo = caminho_campo,
    )

    return app_interno.exists()


def maximizar_janela(caminho_janela: dict) -> bool:
    """Maximiza a janela de um objeto do tipo Application."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    try:
        # localiza o elemento até o final da árvore de parantesco do app
        app_interno = _localizar_elemento(caminho_janela)

        # maximiza a janela informada
        app_interno.maximize()

        # retorna verdadeiro confirmando a execução da ação
        return True
    except:
        return False


def minimizar_janela(caminho_janela: dict) -> bool:
    """Miniminiza a janela de um objeto do tipo Application."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    try:
        # localiza o elemento até o final da árvore de parantesco do app
        app_interno = _localizar_elemento(caminho_janela)

        # miniminiza a janela informada
        app_interno.minimize()

        # retorna verdadeiro confirmando a execução da ação
        return True
    except:
        return False


def mover_mouse(eixo_x: int, eixo_y: int) -> bool:
    # importa recursos do módulo mouse
    from pywinauto.mouse import move

    if (not isinstance(eixo_x, int)) \
    or (not isinstance(eixo_y, int)):
        raise ValueError('Coordenadas precisam ser do tipo inteiro (int).')

    try:
        move(coords=(eixo_x, eixo_y))

        return True
    except:
        return False


def restaurar_janela(caminho_janela: dict) -> bool:
    """Miniminiza a janela de um objeto do tipo Application."""
    # importa app para o escopo da função
    global APP

    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    try:
        # localiza o elemento até o final da árvore de parantesco do app
        app_interno = _localizar_elemento(caminho_janela)

        # restaura a janela informada
        app_interno.restore()

        # retorna verdadeiro confirmando a execução da ação
        return True
    except:
        return True


def retornar_janelas_disponiveis(
    pid: int,
    estilo_aplicacao = 'win32',
) -> str:
    """Retorna as janelas disponíveis em um
    objeto do tipo Application já em execução."""
    # importa app para o escopo da função
    global APP
    global ESTILO_APLICACAO


    ESTILO_APLICACAO = estilo_aplicacao

    # instancia o objeto application
    APP = _aplicacao(estilo_aplicacao = ESTILO_APLICACAO)


    # conecta a aplicação correspondente ao PID informado
    tempo_espera = 60
    app_interno: Application = _conectar_app(
        pid = pid,
        tempo_espera = tempo_espera,
        estilo_aplicacao = ESTILO_APLICACAO,
    )

    # coleta as janelas disponíveis
    lista_janelas = app_interno.windows()

    # instancia uma lista vazia
    lista_janelas_str = []
    # para cada janela na lista de janelas
    for janela in lista_janelas:
        # coleta e salva o nome da janela
        lista_janelas_str.append(janela.texts()[0])

    # retorna uma lista das janelas coletadas
    return lista_janelas_str


def selecionar_em_campo_lista(
    caminho_campo: dict,
    item: str,
) -> str:
    """Seleciona um dado em um elemento de
    lista em um objeto do tipo Application."""
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # seleciona o item informado
    app_interno.select(item).click_input()

    # captura o índice do ítem selecionado
    indice_selecionado = app_interno.selected_indices()

    # retorna o valor capturado
    return indice_selecionado


def selecionar_em_campo_selecao(caminho_campo: dict, item: str) -> str:
    """Seleciona um dado em um elemento de
    seleção em um objeto do tipo Application."""
    # define estático como falso para trabalhar com elemento dinâmico
    if isinstance(caminho_campo, dict) is False:
        raise ValueError('`caminho_campo` precisa ser do tipo dict.')

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = _localizar_elemento(caminho_campo)

    # seleciona o item informado
    app_interno.select(item).click_input()

    # captura o texto do campo localizado
    valor_capturado = coletar_dado_selecionado(caminho_campo)

    # retorna o valor capturado
    return valor_capturado


def selecionar_menu(caminho_janela: dict, caminho_menu: str) -> bool:
    """Seleciona um item de menu conforme o caminho
    informado em um objeto do tipo Application."""
    # importa app para o escopo da função
    if isinstance(caminho_janela, dict) is False:
        raise ValueError('`caminho_janela` precisa ser do tipo dict.')

    try:
        # localiza o elemento até o final da árvore de parantesco do app
        app_interno = _localizar_elemento(caminho_janela)

        # percorre e clica no menu informado
        app_interno.menu_select(caminho_menu)

        # retorna verdadeiro confirmando a execução da ação
        return True
    except:
        return False


def simular_clique(
    botao: str,
    eixo_x: int,
    eixo_y: int,
    tipo_clique: str = 'unico',
) -> bool:
    """Simula clique do mouse, performando o mouse real."""
    # importa recursos do módulo mouse
    from pywinauto.mouse import click, double_click

    if not botao.upper() in ['ESQUERDO', 'DIREITO']:
        raise ValueError('Informe um botão válido: esquerdo, direito.')

    if not tipo_clique.upper() in ['UNICO', 'DUPLO']:
        raise ValueError(
            'Tipo de clique inválido, escolha entre único e duplo.'
        )
    
    if (not isinstance(eixo_x, int)) or (not isinstance(eixo_y, int)):
        raise ValueError('Coordenadas precisam ser do tipo inteiro (int).')

    if botao.upper() == 'ESQUERDO':
        botao = 'left'
    else:
        botao = 'right'

    try:
        if tipo_clique.upper() == 'UNICO':
            click(button=botao, coords=(eixo_x, eixo_y))
        else:
            double_click(button=botao, coords=(eixo_x, eixo_y))

        return True
    except Exception:
        return False


def simular_digitacao(
    texto: str,
    com_espaco: bool = True,
    com_tab: bool = False,
    com_linha_nova: bool = False,
) -> bool:
    """Simula digitação do teclado, performando o teclado real."""
    # importa recursos do módulo keyboard
    from pywinauto.keyboard import send_keys

    if (not isinstance(com_espaco, bool)) \
    or (not isinstance(com_tab, bool)) \
    or (not isinstance(com_linha_nova, bool)):
        raise ValueError(
            """Informe os parâmetros com_espaco,
                com_tab e com_linha_nova com valor boleano"""
        )

    if (not isinstance(texto, str)):
        raise ValueError('Informe um texto do tipo string.')

    try:
        send_keys(
            keys=texto,
            with_spaces=com_espaco,
            with_tabs=com_tab,
            with_newlines=com_linha_nova,
        )

        return True
    except:
        return False
