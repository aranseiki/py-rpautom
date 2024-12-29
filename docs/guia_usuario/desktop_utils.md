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

A escolha entre cada uma delas vai depender do tipo de elemento que está sendo manipulado. Como cada aplicação tem um jeito diferente de expor os elementos e seus estados, recomendamos estar cada opção e verificar o que melhor se encaixa ao momento.

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

Para realizar o clique em um elemento dentro da aplicação, utilize a função ``capturar_texto``.

#formatting.replace_hierarquia_de_elemento#

### função clicar
:::desktop_utils.clicar

___