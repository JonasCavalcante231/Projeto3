# Participantes do grupo: Erick Rafael da Costa Sobreira, Jonas Cavalcante Mendes, Lincoln Diogo Ferreira de Oliveira
# Projeto de Ouvidoria da FACISA

from operacoesbd import *
from metodos import *

abrirbd = abrirBancoDados('localhost', 'root', 'l02102000d.', 'ouvidoria')

opcao = -1

while opcao != 9:
    print()
    print('----- Ouvidoria Universidade FACISA -----')
    print('1) Listar todas as manifestações')
    print('2) Listar todas as sugestões')
    print('3) Listar todas as reclamações')
    print('4) Listar todos os elogios')
    print('5) Enviar uma manifestação (criar uma nova)')
    print('6) Pesquisar protocolo por número (ID)')
    print('7) Apagar Ocorrência por número(Id)')
    print('8) Alterar titulo e descrição de uma manifestação')
    print('9) Sair')


    opcao = int(input('O que você deseja fazer? '))

    print()

    if opcao == 1:
        listarTodasManifestacoes(abrirbd)

    elif opcao == 2:
        listarTodasSugestoes(abrirbd)

    elif opcao == 3:
        listarTodasReclamacoes(abrirbd)

    elif opcao == 4:
        listarTodasElogios(abrirbd)

    elif opcao == 5:
        criarManifestacao(abrirbd)

    elif opcao == 6:
        pesquisarPorID(abrirbd)

    elif opcao == 7:
        apagarOcorrencia(abrirbd)

    elif opcao == 8:
        alterarManifestacao(abrirbd)

    elif opcao < 1 or opcao > 9:
        print('Entrada inválida')

print('Programa encerrado')

encerrarBancoDados(abrirbd)