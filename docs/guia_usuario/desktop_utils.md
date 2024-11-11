#### Exemplo de código com a função iniciar_app

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


executavel = r"C:\Windows\notepad.exe"
estilo_aplicacao = 'uia'
# Parâmetro ``esperar`` exige, se for especificado, ser do tipo tupla,
#   onde é preciso passar as seguintes informações:
#   Na primeira opção da tupla, a condiçõa esperada para validar a
#   aplicação como instanciada com sucesso. Recebe os valores: 'exists',
#   'visible', 'enabled', 'ready', e 'active'. Na segunda opção da tupla,
#   o valor limite, em segundos, da tentativa de instanciar a aplicação.
esperar=()
#   Parâmetro ``inverter`` inverte logicamente a condição de espera para
#   tornar a expressão negativa como aceita. Ex.: inverter == True e
#   esperar == ('visible', _) faz a aplicação esperar o programa não ficar
#   visível. Portanto, inverte a lógica do estado no parâmetro esperar.
inverter = False
# Parâmetro ``ocioso`` determina se a função aguardará ou não até que a
#   aplicação esteja pronta após iniciá-la.
ocioso = False
# O retorno da função é um inteiro do PID atrelado à aplicação manipulada.
desktoputils.iniciar_app(
    executavel = executavel,
    estilo_aplicacao = estilo_aplicacao,
    esperar = esperar,
    inverter = inverter,
    ocioso = ocioso,
)


```

#### Exemplo de código com a função conectar_app

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


# A função conectar_app tem como objetivo conectar uma aplicação no
#   conjunto de aplicações manipuladas na execução. A diferente dela
#   para a iniciar_app é que a iniciar_app inicia um processo novo a
#   partir de um caminho de executável, já a conectar_app conecta um
#   processo já existente à manipulação.
pid = 3960
tempo_espera = 10
estilo_aplicacao = 'uia'
desktoputils.conectar_app(
    pid = pid,
    tempo_espera = tempo_espera,
    estilo_aplicacao = estilo_aplicacao,
)


```

#### Exemplo de código com a função retornar_janelas_disponiveis

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


pid = 3960
estilo_aplicacao = 'win32'
desktoputils.retornar_janelas_disponiveis(
    pid = pid,
    estilo_aplicacao = estilo_aplicacao,
)

```

#### Exemplo de código com a função localizar_elemento

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


# Retorna se o caminho de elementos informado existe
#   no programa sendo manipulado.
# O parâmetro ``estatico`` informa se o campo é editável,
#   aceitando valor boleano.
caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
estatico = False
desktoputils.localizar_elemento(
    caminho_campo = caminho_campo,
    estatico = estatico,
)


```

#### Exemplo de código com a função _localizar_elemento

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


# Retorna o objeto do tipo Application da biblioteca PyWinAuto
#   com o caminho de elementos informado.
# O parâmetro ``estatico`` informa se o campo é editável,
#   aceitando valor boleano.
caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
estatico = True
desktoputils._localizar_elemento(
    caminho_campo = caminho_campo,
    estatico = estatico,
)

```

#### Exemplo de código com a função capturar_texto

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
estatico = True
desktoputils.capturar_texto(
    caminho_campo = caminho_campo,
    estatico = estatico,
)


```

#### Exemplo de código com a função coletar_arvore_elementos

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
estatico = True
desktoputils.coletar_arvore_elementos(
    nome_janela = nome_janela,
    estatico = estatico,
)


```

#### Exemplo de código com a função localizar_diretorio_em_treeview

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
caminho_diretorio = 'caminho_diretorio'
estatico = True
desktoputils.localizar_diretorio_em_treeview(
    caminho_janela = caminho_campo,
    caminho_diretorio = caminho_diretorio,
    estatico = estatico,
)

```

#### Exemplo de código com a função digitar

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
valor = 'str'
com_espaco = True,
digitacao_visivel = True,
com_nova_linha = False,
desktoputils.digitar(
    caminho_campo = caminho_campo,
    valor = valor,
    com_espaco = com_espaco,
    digitacao_visivel = digitacao_visivel,
    com_nova_linha = com_nova_linha,
)


```

#### Exemplo de código com a função clicar

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
desktoputils.clicar(caminho_campo = caminho_campo)


```

#### Exemplo de código com a função simular_clique

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


botao = 'direito'
eixo_x = 100
eixo_y = 100
tipo_clique = 'unico'
desktoputils.simular_clique(
    botao = botao,
    eixo_x = eixo_x,
    eixo_y = eixo_y,
    tipo_clique = tipo_clique,
)

```

#### Exemplo de código com a função simular_digitacao

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


texto = 'str'
com_espaco = True
com_tab = False
com_linha_nova = True
desktoputils.simular_digitacao(
    texto = texto,
    com_espaco = com_espaco,
    com_tab = com_tab,
    com_linha_nova = com_linha_nova,
)


```

#### Exemplo de código com a função mover_mouse

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


eixo_x = 100
eixo_y = 100
desktoputils.mover_mouse(
    eixo_x = eixo_x,
    eixo_y = eixo_y,
)

```

#### Exemplo de código com a função coletar_situacao_janela

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.coletar_situacao_janela(nome_janela = nome_janela)

```

#### Exemplo de código com a função esta_visivel

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.esta_visivel(nome_janela = nome_janela)


```

#### Exemplo de código com a função janela_existente

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


pid = 3960
nome_janela = 'Untitled - Notepad'
desktoputils.janela_existente(pid = pid, nome_janela = nome_janela)

```

#### Exemplo de código com a função esta_com_foco

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.esta_com_foco(nome_janela = nome_janela)


```

#### Ativando foco em uma janela

Para colocar a janela em evidência, utilize a função ``ativar_foco``.
Nela, passe como parâmetro o nome de uma janela que já está em manipulação
pela biblioteca. Isso significa que o nome precisa ser válido dentre as opções
dos nomes de janelas que já são manipuláveis.

A função retorna booleano. Caso o foco dê certo, ``True``. Caso o foco dê errado, ``False``.

:::desktop_utils.ativar_foco

#### Exemplo de código com a função minimizar_janela

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.minimizar_janela(nome_janela = nome_janela)


```

#### Exemplo de código com a função maximizar_janela

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.maximizar_janela(nome_janela = nome_janela)

```

#### Exemplo de código com a função restaurar_janela

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
desktoputils.restaurar_janela(nome_janela = nome_janela)

```

#### Exemplo de código com a função coletar_dados_selecao

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
desktoputils.coletar_dados_selecao(caminho_campo = caminho_campo)

```

#### Exemplo de código com a função coletar_dado_selecionado

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
desktoputils.coletar_dado_selecionado(caminho_campo = caminho_campo)

```

#### Exemplo de código com a função selecionar_em_campo_selecao

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
item = ''
desktoputils.selecionar_em_campo_selecao(caminho_campo = caminho_campo, item = item)

```

#### Exemplo de código com a função selecionar_em_campo_lista

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


caminho_campo = 'Untitled - Notepad->DesktopWindowXamlSource'
item = ''
desktoputils.selecionar_em_campo_lista(caminho_campo = caminho_campo, item = item)

```

#### Exemplo de código com a função selecionar_menu

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


nome_janela = 'Untitled - Notepad'
caminho_menu = 'File->Open'
desktoputils.selecionar_menu(
    nome_janela = nome_janela,
    caminho_menu = caminho_menu,
)


```

#### Exemplo de código com a função fechar_janela

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils

nome_janela = 'Untitled - Notepad'
desktoputils.fechar_janela(nome_janela = nome_janela)

```

#### Exemplo de código com a função encerrar_app

``` {.py3 title="main.py"}
from py_rpautom import automacao_desktop_utils as desktoputils


pid = 18212
forcar = True
tempo_espera = 2
desktoputils.encerrar_app(
    pid = pid,
    forcar = forcar,
    tempo_espera = tempo_espera,
)


```
