from operacoesbd import *

listaTipo = ['Sugestão', 'Reclamação', 'Elogio']


def listarTodasManifestacoes(abrirbd):
    print()
    print('Listar todas as manifestações')
    print()

    listardbgeral = 'select * from ouvidoriaMani'

    manifestacoes = listarBancoDados(abrirbd, listardbgeral)

    for manifestacao in manifestacoes:
        print('Código: {} - Requisitante: {} - Tipo: {} - Descrição: {}'.format(
            manifestacao[0], manifestacao[1], manifestacao[2], manifestacao[3]))


def listarTodasSugestoes(abrirbd):
    print()
    print('Listar todas as sugestões')
    print()

    listarsugestoes = 'select * from ouvidoriaMani where tipo = "Sugestão"'

    sugestoes = listarBancoDados(abrirbd, listarsugestoes)

    for sugestao in sugestoes:
        print('Código: {} - Requisitante: {} - Descrição: {}'.format(
            sugestao[0], sugestao[1], sugestao[3]))


def listarTodasReclamacoes(abrirbd):
    print()
    print('Listar todas as reclamações')
    print()

    listarreclamacoes = 'select * from ouvidoriaMani where tipo = "Reclamacão"'

    reclamacoes = listarBancoDados(abrirbd, listarreclamacoes)

    for reclamacao in reclamacoes:
        print('Código: {} - Requisitante: {} - Descrição: {}'.format(
            reclamacao[0], reclamacao[1], reclamacao[3]))


def listarTodasElogios(abrirbd):
    print()
    print('Listar todos os elogios')
    print()

    listarelogios = 'select * from ouvidoriaMani where tipo = "Elogio"'

    elogios = listarBancoDados(abrirbd, listarelogios)

    for elogio in elogios:
        print(
            'Código: {} - Requisitante: {} - Descrição: {}'.format(elogio[0], elogio[1], elogio[3]))


def criarManifestacao(abrirbd):
    print('Enviar uma manifestação (criar uma nova)')
    print()
    nome = str(input('Digite o nome do requisitante: '))
    print()
    tipo = int(input(
        'Digite o tipo de manifestação (Digite 1 para sugestão, 2 para reclamação e 3 para elogio): '))
    print()

    descricao = str(input('Digite a descrição: '))

    inserirsql = 'insert into ouvidoriaMani(nome, tipo, descricao) values(%s, %s, %s)'
    dados = (nome, listaTipo[tipo-1], descricao)

    insertNoBancoDados(abrirbd, inserirsql, dados)


def pesquisarPorID(abrirbd):
    print('Pesquisar protocolo por número (ID)')
    print()
    idEscolha = str(input('Digite o número do protocolo: '))
    print()

    listarEscolhido = 'select * from ouvidoriaMani where id =' + idEscolha
    resultadoPesquisa = listarBancoDados(abrirbd, listarEscolhido)

    itemPesquisado = resultadoPesquisa[0]
    elementos = list(itemPesquisado)

    print('Código: {}'.format(elementos[0]))
    print('Requisitante: {}'.format(elementos[1]))
    print('Tipo: {}'.format(elementos[2]))
    print('Descrição: {}'.format(elementos[3]))

def apagarOcorrencia(abrirbd):
    codigo = input('digite o código da manisfestação: ')
    consultaListagem = 'DELETE FROM manifestacao WHERE codigo = %s'
    dados = [codigo]
    linhasAfetadas = excluirBancoDados(abrirbd,connection,consultaListagem, dados)

    if linhasAfetadas > 2:
        print('Manifestação excluída com sucesso!')
    else:
        print('Nenhuma manifestação encontrada com o código fornecido')


def alterarManifestacao(abrirbd):
    codigo = input('digite o código da manifestação que deseja alterar: ')
    novoTitulo = input('digite o novo titulo da manifestação: ')
    novaDescricao = input('digite a nova descrição da manifestação: ')

    sqlAtualizar = 'UPDATE ocorrencias SET titulo = %s, descricao = %s WHERE codigo = %s'
    valores = [novoTitulo, novaDescricao, codigo]
    linhasAfetadas = atualizarBancoDados(abrirbd,sqlAtualizar,valores)

    if linhasAfetadas > 0:
        print('Atualizado com sucesso!')
    else:
        print('nenhuma manifestação encontrada com o código informado!')