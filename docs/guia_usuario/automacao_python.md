#### Exemplo de código usando a função remover_acentos

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


pyutils.cls()


```
#### Exemplo de código usando a função remover_acentos

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils

texto = '''João come açaí com o crachá depois do trabalho. Já Maria, joga dominó ao voltar da escola para casa.
 Às vezes, parece que é fácil ouvir um álbum de artistas célebres enquanto cria um gráfico das últimas reuniões.'''
pyutils.remover_acentos(
    texto,
    normalizacao='NFKD',
)


```
#### Exemplo de código usando a função logar

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


mensagem = 'Mensagem para log'
nivel = 'INFO'
pyutils.logar( #
    mensagem,
    nivel,
    arquivo=None,
    modo=None,
    encoding=None,
    formatacao=None,
    handlers=None,
)


```
#### Exemplo de código usando a função criar_pasta

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'pasta_exemplo'
pyutils.criar_pasta(caminho)


```
#### Exemplo de código usando a função criar_arquivo_texto

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivo_texto_exemplo.txt'
dado='Dado de exemplo para arquivo de texto'
pyutils.criar_arquivo_texto (
    caminho=caminho,
    dado=dado,
    encoding='utf8',
    em_bytes = False,
)


```
#### Exemplo de código usando a função caminho_existente

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


# em caso de o caminho existir
caminho = 'arquivo_texto_exemplo.txt'

# em caso de o caminho não existir
# caminho = 'arquivo_textao_exemplo.txt'

pyutils.caminho_existente(caminho)


```
#### Exemplo de código usando a função abrir_arquivo_texto

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivo_texto_exemplo.txt'
pyutils.abrir_arquivo_texto(caminho, encoding='utf8')


```
#### Exemplo de código usando a função abrir_arquivo_excel

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo_excel = 'arquivo_excel_exemplo.xlsx'
guia = 'aba_exemplo'
pyutils.abrir_arquivo_excel(
    arquivo_excel,
    guia,
    manter_macro = True,
    manter_links = True,
)


```
#### Exemplo de código usando a função abrir_arquivo_word

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo_word = 'arquivos_exemplo/arquivo_word_exemplo.docx'
pyutils.abrir_arquivo_word(arquivo_word = arquivo_word,)


```
#### Exemplo de código usando a função abrir_arquivo_pdf

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo_pdf = 'arquivos_exemplo/arquivo_pdf_exemplo.pdf'
# ``paginacao`` aceita inteiro ou lista/tupla de inteiros,
    # sendo que 0 corresponde à todas as páginas
paginacao = 0
# ``orientacao`` aceita apenas inteiro, sendo um dos quatro valores seguintes:
    # 0 (para cima),
    # 90 (virado para a esquerda),
    # 180 (de cabeça para baixo),
    # 270 (virado para a direita)
orientacao = 0,
pyutils.abrir_arquivo_pdf(
    arquivo_pdf = arquivo_pdf,
    senha_pdf = None,
    paginacao = paginacao,
    orientacao = orientacao,
)


```
#### Exemplo de código usando a função abrir_arquivo_em_bytes

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/arquivo_pdf_exemplo.pdf'
pyutils.abrir_arquivo_em_bytes(caminho)


```
#### Exemplo de código usando a função escrever_em_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
conteudo = 'Exemplo de código usando a função escrever_em_arquivo'
modo='w'
pyutils.escrever_em_arquivo(
    arquivo,
    conteudo = conteudo,
    modo = modo,
    encoding='utf8',
    nova_linha=None,
)


```
#### Exemplo de código usando a função gravar_log_em_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
conteudo = ('Exemplo de código', 'usando a função', 'gravar_log_em_arquivo\n',)
modo='a'
pyutils.gravar_log_em_arquivo(
    arquivo = arquivo,
    conteudo = conteudo,
    modo = modo,
    encoding='utf8',
    delimitador=';',
    nova_linha='\r\n',
)


```
#### Exemplo de código usando a função coletar_nome_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
pyutils.coletar_nome_arquivo(caminho)


```
#### Exemplo de código usando a função coletar_extensao_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
pyutils.coletar_extensao_arquivo(caminho)


```
#### Exemplo de código usando a função coletar_caminho_absoluto

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
pyutils.coletar_caminho_absoluto(caminho)


```
#### Exemplo de código usando a função coletar_arvore_caminho

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
pyutils.coletar_arvore_caminho(caminho)


```
#### Exemplo de código usando a função coletar_nome_guias_arquivo_excel

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo_excel = 'arquivos_exemplo/arquivo_excel_exemplo.xlsx'
pyutils.coletar_nome_guias_arquivo_excel(arquivo_excel)


```
#### Exemplo de código usando a função converter_pdf_em_imagem

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo_pdf = 'arquivos_exemplo/arquivo_pdf_exemplo.pdf'
caminho_saida = 'arquivos_exemplo/caminho_retorno'
# ``zoom`` aceita inteiro ou flutuante, sendo de 1 à 9.x, onde 1 é o normal.
zoom = 1
# ``orientacao`` aceita apenas inteiro, sendo um dos quatro valores seguintes:
    # 0 (para cima),
    # 90 (virado para a esquerda),
    # 180 (de cabeça para baixo),
    # 270 (virado para a direita)
orientacao = 0
pyutils.converter_pdf_em_imagem(
    arquivo_pdf = arquivo_pdf,
    caminho_saida = caminho_saida,
    alpha = False,
    zoom = zoom,
    orientacao = orientacao,
)


```
#### Exemplo de código usando a função extrair_texto_ocr

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils

arquivo = 'arquivos_exemplo/caminho_retorno/arquivo_218.png'
linguagem = 'por'
pyutils.extrair_texto_ocr(arquivo, linguagem, encoding='utf8')


```
#### Exemplo de código usando a função retornar_arquivos_em_pasta

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/caminho_retorno/'
pyutils.retornar_arquivos_em_pasta(caminho, filtro='**/*')


```
#### Exemplo de código usando a função retornar_data_hora_atual

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


parametro = '%d_%m_%Y'
pyutils.retornar_data_hora_atual(parametro)


```
#### Exemplo de código usando a função alterar_arquivo_texto

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


# alterar_arquivo_texto substitui linhas inteiras
#   onde a mesma contém o conteúdo fornecido pelo
#   parâmetro ``linha_atual``, e troca esse conteúdo
#   pelo informado em ``linha_alterada``.
caminho = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
linha_atual = 'Exemplo de código;usando a função;gravar_log_em_arquivo'
linha_alterada = 'Texto alterado'
# Parâmetro ``multilinhas`` serve para substutuir todas as linhas
multilinhas = True
pyutils.alterar_arquivo_texto(
    caminho = caminho,
    linha_atual = linha_atual,
    linha_alterada = linha_alterada,
    multilinhas = multilinhas,
    encoding_entrada='utf8',
    encoding_saida='utf8',
)


```
#### Exemplo de código usando a função copiar_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo = 'arquivos_exemplo/arquivo_texto_exemplo.txt'
caminho_destino = 'arquivos_exemplo/caminho_retorno/'
pyutils.copiar_arquivo(arquivo, caminho_destino)


```
#### Exemplo de código usando a função copiar_pasta

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


pasta = 'arquivos_exemplo/caminho_retorno'
caminho_destino = 'arquivos_exemplo/caminho_retorno/'
pyutils.copiar_pasta(pasta, caminho_destino)


```
#### Exemplo de código usando a função renomear

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = './arquivos_exemplo/caminho_retorno/caminho_retorno'
nome_atual = 'arquivo_1.png'
novo_nome = 'arquivo.png'
pyutils.renomear(caminho, nome_atual, novo_nome)


```
#### Exemplo de código usando a função recortar

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho_atual = 'arquivos_exemplo/caminho_retorno/caminho_retorno/arquivo.png'
caminho_novo = 'arquivos_exemplo/caminho_retorno/'
pyutils.recortar(caminho_atual, caminho_novo)


```
#### Exemplo de código usando a função descompactar

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


arquivo = 'atuacao_ole_siscob.zip'
caminho_destino = './arquivos_exemplo/'
pyutils.descompactar(arquivo, caminho_destino, senha_arquivo=None)


```
#### Exemplo de código usando a função coletar_idioma_so

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


pyutils.coletar_idioma_so()


```
#### Exemplo de código usando a função coletar_pid

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


nome_processo = 'msedge'
pyutils.coletar_pid(nome_processo)


```
#### Exemplo de código usando a função ler_variavel_ambiente

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils

# Esta função coleta valores de variáveis, de sistema
#   ou contido em um arquivo. Para caso queira usar em
#   arquivo, defina um arquivo de configuração .ini e
#   formate em blocos. Nesse caso, é possível coletar o
#   bloco inteiro ou apenas uma variável do bloco. Para
#   coletar o bloco inteiro, não defina o parâmetro
#   ``nome_variavel`` e caso queira exclusivamente uma
#   variável, a referencie nesse parâmetro. Nos dois
#   casos usando o arquivo é preciso definir o parâmetro
#   ``nome_bloco_config``.
nome_variavel='username'
variavel_sistema = True
pyutils.ler_variavel_ambiente(
    arquivo_config='',
    nome_bloco_config='',
    nome_variavel = nome_variavel,
    variavel_sistema = variavel_sistema,
    encoding = 'utf8',
)


```
#### Exemplo de código usando a função processo_existente

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


nome_processo = 'calc'
pyutils.processo_existente(nome_processo)


```
#### Exemplo de código usando a função finalizar_processo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


pid = 14464
pyutils.finalizar_processo(pid)


```
#### Exemplo de código usando a função janela_dialogo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


# Cria uma janela de opções com botões como OK ou CANCEL, ou ainda ABORT.
#   Essa janela tem como manipulação um objeto nativo do sistema, e por
#   então são apresentados elementos nativos. O retorno da função é um
#   inteiro correspondente à opção selecionada.
#   O parâmetro ``estilo`` é responsável pela escolha das opções de botões
#   que deverão aparecer, sendo necessário informar um número de 0 à 6.
titulo = 'arquivo_pdf_exemplo.pdf'
texto = 'Arquivo de exemplo'
estilo = 0
pyutils.janela_dialogo(titulo, texto, estilo)


```
#### Exemplo de código usando a função excluir_arquivo

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/caminho_retorno/arquivo.png'
pyutils.excluir_arquivo(caminho)


```
#### Exemplo de código usando a função pasta_esta_vazia

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/caminho_retorno/'
pyutils.pasta_esta_vazia(caminho = caminho)


```
#### Exemplo de código usando a função excluir_pasta

``` {.py3 title="main.py"}
from py_rpautom import python_utils as pyutils


caminho = 'arquivos_exemplo/caminho_retorno/'
vazia = False
pyutils.excluir_pasta(caminho, vazia = vazia)


```
