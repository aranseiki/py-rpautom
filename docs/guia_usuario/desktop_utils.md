# Módulo desktop_utils (desktop_utils.py)
___

Para realizar automações em aplicações desktop, de interface gráfica, utilize este módulo. Abaixo, detalhamento das funções suas utilizações:

## Estrutura de hierarquia de um elemento:

#formatting.replace_caminho_campo#

## Ativando foco em uma janela

Para colocar a janela em evidência, utilize a função ``ativar_foco``.
Nela, passe como parâmetro o nome de uma janela que já está em manipulação
pela aplicação. Isso significa que o nome precisa ser válido dentre as opções
dos nomes de janelas que já são manipuláveis.

A função retorna booleano. Caso o foco dê certo, ``True``. Caso o foco dê errado, ``False``.

### função ativar_foco
:::desktop_utils.ativar_foco

___

## Verificando se um botão de seleção está marcado

Para verificar se um botão de seleção do tipo checkbox está marcado, utilize a função ``botao_esta_marcado``.
Esta função verifica se o botão está selecionado, retornando um valor booleano. ``True`` caso o botão estiver selecionado, ``False`` caso o botão não estiver selecionado. Para utilizá-la, basta no momento da chamada, informar os seguintes dados:

> caminho até o elemento em formato dict (caminho_campo) :

#formatting.replace_hierarquia_de_elemento#

> opcao de verificacao (opcao_verificacao) :

Existem 3 tipos de verificações:

* 'IS_CHECKED': É a verificação pura se está selecionado.
* 'GET_CHECK_STATE': Coleta o estado do elemento (se selecionado ou não).
* 'GET_SHOW_STATE': Coleta a exibição gráfica do estado do elemento (se selecionado ou não).

A escolha entre cada uma delas vai depender do tipo de elemento que está sendo manipulado. Como cada aplicação tem um jeito diferente de expor os elementos e seus estados, recomendamos testar cada opção e verificar o que melhor se encaixa ao momento.

### função botao_esta_marcado
:::desktop_utils.botao_esta_marcado

___

## Capturando imagem de um elemento

Existe um recurso para tirar uma imagem do elemento no estado atual da execução. Para isso, utilize a função ``capturar_imagem``.

#formatting.replace_hierarquia_de_elemento#

### função capturar_imagem
:::desktop_utils.capturar_imagem

___

## Coletando propriedades de um elemento

Algumas vezes serão necessárias algumas informações, como a posição do elemento na aplicação, se o elemento está em unicode ou mesmo nome da classe ou control_id. Para coletar estas e outras informações de um elemento, utilize a função ``capturar_propriedade_elemento``.

#formatting.replace_hierarquia_de_elemento#

### função capturar_propriedade_elemento
:::desktop_utils.capturar_propriedade_elemento

___

## Coletando o texto de um elemento

Um recurso muito comum é a captura de texto de um elemento. Para este feito, utilize a função ``capturar_texto``.

#formatting.replace_hierarquia_de_elemento#

### função capturar_texto
:::desktop_utils.capturar_texto

___


## Clicando em um elemento

Para realizar o clique em um elemento dentro da aplicação, utilize a função ``clicar``.

#formatting.replace_hierarquia_de_elemento#

### função clicar
:::desktop_utils.clicar

___


## Coletando a árvore de elementos de uma janela ou elemento

Utilizando a função ``coletar_arvore_elementos``, é possível verificar quais elementos compõem uma janela ou um elemento específico. A abordagem é única para ambos os casos.

Uma árvore de elementos é a estrutura hierárquica dos elementos em uma aplicação. Dentro de uma jánela há elementos. Esses elementos podem ou não conter elementos dentro de si. Isso vai compondo uma hierarquização de elementos, um dentro de outro, ao lado de outro e assim por diante.

Assim, para visualizar a estrutura de um elemento ou de uma janela, recorra à função coletar_arvore_elementos. Ela retorna, em string, os elementos dentro do que foi solicitado. Caso, por exemplo, seja informado no parâmetro ``caminho_elemento`` uma janela, será retornado todos os elementos visíveis dessa janela no momento da execução do comando. O mesmo acontece caso seja passado um elemento.

#formatting.replace_hierarquia_de_elemento#

### função coletar_arvore_elementos
:::desktop_utils.coletar_arvore_elementos

___


## Coletando valor selecionado de um campo de seleção

Um campo de seleção, elemento do tipo combobox, sempre contém alguma opção selecionada, mesmo que seja um valor vazio ou definido por padrão pela aplicação. Caso queira coletar o valor de um campo de seleção, utilize a função abaixo, que retornará o valor do campo informado no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função coletar_dado_selecionado
:::desktop_utils.coletar_dado_selecionado

___


## Coletando valores disponíveis de um campo de seleção

Assim como um campo de seleção, elemento do tipo combobox, contém alguma opção selecionada, também contem uma ou mais opções para selecionar. Para coletar todos os valores disponíveis em um campo de seleção, utilize a função abaixo, que retornará, em string, as opções de seleção do elemento solicitado no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função coletar_dados_selecao
:::desktop_utils.coletar_dados_selecao

___


## Coletando o estado atual da janela

As janelas de uma aplicação dentro de um sistema operacional tem estados padrões, como estar minimizado ou em modo normal. Estes e outros estados podem ser capturados utilizando a função ``coletar_situacao_janela`` no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função coletar_situacao_janela
:::desktop_utils.coletar_situacao_janela

___


## Conectando-se à uma aplicação já em execução

É possível manipular aplicações já em execução. Para isso, utilize a função ``conectar_app``, que adicionará a aplicação ao conjunto de aplicações manipuláveis e retornará o PID da mesma.

### função conectar_app
:::desktop_utils.conectar_app

#formatting.replace_estilo_aplicacao#

___


## Digitando em um elemento

Para escrever algum texto ou número em um elemento, utilize a função ``digitar``. Em caso de número, deve ser enviado em formato string.

#formatting.replace_hierarquia_de_elemento#

### função digitar
:::desktop_utils.digitar

___


## Fechando uma aplicação

Para fechar uma aplicação e todas as suas janelas abertas, utilize a função ``encerrar_app``.

### função encerrar_app
:::desktop_utils.encerrar_app

___


## Coletando o estado de foco atual da janela

As janelas de uma aplicação dentro de um sistema operacional tem estados de focos padrões, com foco ou sem foco. Estes estados de foco podem ser capturados utilizando a função ``esta_com_foco``, que retorna a situação do foco da janela no momento de sua execução.

### função esta_com_foco
:::desktop_utils.esta_com_foco

___


## Coletando o estado de visibilidade atual de uma janela

As janelas de uma aplicação dentro de um sistema operacional tem estados de visibilidade padrões, como visível ou não visível. Entende-se por visível, a situação da janela onde está em estado 'maximizado' ou 'normal'. E não visível para 'minimizado'. Estes estados de visibilidade podem ser capturados utilizando a função ``esta_visivel``, que retorna a situação de visibilidade da janela no momento de sua execução.

### função esta_visivel
:::desktop_utils.esta_visivel

___


## Fechando uma janela de uma aplicação

Para fechar uma janela aberta de uma aplicação, utilize a função ``fechar_janela``.

### função fechar_janela
:::desktop_utils.fechar_janela

___


## Iniciando uma aplicação

Para iniciar e abrir uma aplicação, utilize a função ``iniciar_app`` conforme descrito abaixo.

### função iniciar_app
:::desktop_utils.iniciar_app

___


## Coletando o estado de existência atual de uma janela

Para verificar se uma janela de uma aplicação existe, utilize a função ``janela_existente``.

### função janela_existente
:::desktop_utils.janela_existente

___


## Selecionando um caminho em uma lista de diretórios

Para selecionar um caminho em uma lista hierárquica de diretórios, elemento do tipo treeview, utilize a função ``localizar_diretorio_em_treeview``.

#formatting.replace_hierarquia_de_elemento#

### função localizar_diretorio_em_treeview
:::desktop_utils.localizar_diretorio_em_treeview

___


## Localizando uma janela ou elemento em uma janela

É possível verificar se uma janela ou um elemento dentro de uma janela na estrutura de elementos da aplicação que está sendo manipulado existe através da função ``localizar_elemento``.

#formatting.replace_hierarquia_de_elemento#

### função localizar_elemento
:::desktop_utils.localizar_elemento

___


## Maximizando uma janela

As janelas de uma aplicação dentro de um sistema operacional tem estados padrões, como estar maximizado. utilize a função ``maximizar_janela`` para, no momento de sua execução, alterar uma janela para maximizado.

#formatting.replace_hierarquia_de_elemento#

### função maximizar_janela
:::desktop_utils.maximizar_janela

___


## Minimizando uma janela

As janelas de uma aplicação dentro de um sistema operacional tem estados padrões, como estar minimizado. utilize a função ``minimizar_janela`` para, no momento de sua execução, alterar uma janela para minimizado.

#formatting.replace_hierarquia_de_elemento#

### função minimizar_janela
:::desktop_utils.minimizar_janela

___


## Movendo o mouse

Há um recurso para movimentação do mouse até um ponto específico da tela, mediante coordenadas de eixo X e Y. As coordenadas precisam ser informadas em pixels e representam o posicionamento de pixels da tela. Para isso, utilize a função ``mover_mouse``.

### função mover_mouse
:::desktop_utils.mover_mouse

___


## Restaurando uma janela

As janelas de uma aplicação dentro de um sistema operacional tem estados padrões, como estar restaurado. utilize a função ``restaurar_janela`` para, no momento de sua execução, alterar uma janela para restaurado.

#formatting.replace_hierarquia_de_elemento#

### função restaurar_janela
:::desktop_utils.restaurar_janela

___

## Verificando janelas disponíveis

Um recurso muito comum é a verificação das janelas existentes de uma aplicação em execução. Para coletar todos os nomes de janelas disponíveis de uma aplicação em execução e que está sendo manipulada, utilize a função abaixo, que retornará, em string, os nomes coletados no momento de sua execução.

### função retornar_janelas_disponiveis
:::desktop_utils.retornar_janelas_disponiveis

#formatting.replace_estilo_aplicacao#

___


## Selecionando uma aba disponível

Para em um elemento de conjunto de abas, elemento do tipo tab control, selecionar alguma opção das opções de abas disponíveis, utilize a função abaixo, que retornará, em booleano, se a aba foi selecionada no momento de sua execução.
É possível selecionar a aba informando o número correspondente da aba, ou seu nome, através do parâmetro ``item``.

#formatting.replace_hierarquia_de_elemento#

### função selecionar_aba
:::desktop_utils.selecionar_aba

___


## Selecionando um valor em um campo de listas

Para em um campo de listas, elemento do tipo listbox, selecionar alguma opção das opções da listagem disponível, utilize a função abaixo, que retornará, em booleano, se a opção foi selecionada no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função selecionar_em_campo_lista
:::desktop_utils.selecionar_em_campo_lista

___


## Selecionando um valor em um campo de seleção

Para em um campo de seleção, elemento do tipo combobox, selecionar alguma opção das opções disponíveis, utilize a função abaixo, que retornará, em string, o valor do campo informado alterado no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função selecionar_em_campo_selecao
:::desktop_utils.selecionar_em_campo_selecao

___


## Selecionando um item de menu

Para em menu, elemento do tipo MenuBar, selecionar alguma opção dos itens de menu disponíveis, utilize a função abaixo, que retornará, em booleano, se o item de menu foi selecionado no momento de sua execução.

#formatting.replace_hierarquia_de_elemento#

### função selecionar_menu
:::desktop_utils.selecionar_menu

___


## Simulando clique do mouse

Há um recurso para disparar eventos de clique do mouse em um ponto específico da tela, mediante coordenadas de eixo X e Y. As coordenadas precisam ser informadas em pixels e representam o posicionamento de pixels da tela. Para isso, utilize a função ``simular_clique``.

### função simular_clique
:::desktop_utils.simular_clique

___


## Simulando digitação do teclado

Há um recurso para disparar eventos de digitação do teclado em um ponto específico da tela, mediante coordenadas de eixo X e Y. As coordenadas precisam ser informadas em pixels e representam o posicionamento de pixels da tela. Para isso, utilize a função ``simular_digitacao``.

### função simular_digitacao
:::desktop_utils.simular_digitacao
