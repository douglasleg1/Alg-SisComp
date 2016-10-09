 # {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" },
# BLACK : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
import time
from random import randint
print('                            Sejam bem vindos ao DDMChess!!!\n'
      '                 Jogo produzido por: Douglas Dantas e Marlon Costa \n')

#FUNÇÃO PARA RECEBER OS NOMES DOS JOGADORES
def nomes_jogadores():
    '''Define o nome dos jogadores'''

    while True:
        player1 = input("Digite o nome do Player 1 (BRANCAS): ")

        while player1 == '':
            print('\nJogador 1 com nome vazio!\n')
            player1 = input("Digite o nome do Player 1 (BRANCAS):: ")

            if player1 != '':
                break

        player2 = input("Digite o nome do Player 2 (PRETAS): ")
        while player2 == '':
            print('\nJogador 2 com nome vazio!\n')
            player2 = input("Digite o nome do Player 2 (PRETAS): ")

            if player2 != '':
                break

        if player1 == player2:
            print('\nJogadores com mesmo nome, diferencie-os em algo.\n')
            continue

        return player1, player2

#FUNÇÃO PARA IMPRIMIR A INTERFACE DO TABULEIRO
def interface():
    '''Cria a interface'''
    print('\n')
    print('     ♚♛♗♞♖♟ DDMChess ♟♖♞♗♛♚ \n')
    print("   A    B    C    D    E    F    G    H")
    print("  ____ ____ ____ ____ ____ ____ ____ ____")
    print("1| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[0][0], tab[0][1], tab[0][2], tab[0][3], tab[0][4], tab[0][5], tab[0][6], tab[0][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("2| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[1][0], tab[1][1], tab[1][2], tab[1][3], tab[1][4], tab[1][5], tab[1][6], tab[1][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("3| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[2][0], tab[2][1], tab[2][2], tab[2][3], tab[2][4], tab[2][5], tab[2][6], tab[2][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("4| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[3][0], tab[3][1], tab[3][2], tab[3][3], tab[3][4], tab[3][5], tab[3][6], tab[3][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("5| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[4][0], tab[4][1], tab[4][2], tab[4][3], tab[4][4], tab[4][5], tab[4][6], tab[4][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("6| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[5][0], tab[5][1], tab[5][2], tab[5][3], tab[5][4], tab[5][5], tab[5][6], tab[5][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("7| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[6][0], tab[6][1], tab[6][2], tab[6][3], tab[6][4], tab[6][5], tab[6][6], tab[6][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print("8| %s | %s | %s | %s | %s | %s | %s | %s |" % (
        tab[7][0], tab[7][1], tab[7][2], tab[7][3], tab[7][4], tab[7][5], tab[7][6], tab[7][7]))
    print(" |____|____|____|____|____|____|____|____|")
    print('\n    ♚♛♗♞♖♟ DDMChess ♟♖♞♗♛♚ \n')

#FUNÇÃO PARA RECEBER A PEÇA SELECIONADA PELO USUÁRIO
def seleciona_peca():
    '''Dá a posição inicial da peça a ser movida, seu tipo e sua cor'''
    while True:

        try:
            pos_inicial = input(
                '%s, escolha uma peça para jogar no seguinte padrão: %s%s\n' % (player, letras[randint(0,7)],randint(0,7))).lower()
            pos_inic = ['', '']
            pos_inic[0] = letras.index(pos_inicial[0])
            pos_inic[1] = int(pos_inicial[1]) - 1

            peca = tab[pos_inic[1]][pos_inic[0]]

            if player == player1 and peca.startswith('b'):
                print('\nA peça não lhe pertence %s, tente novamente!\n' % player)
                interface()
                continue

            elif player == player2 and peca.startswith('w'):
                print('\nA peça não lhe pertence %s, tente novamente!\n' % player)
                interface()
                continue

            if peca == '  ':
                print('\nCasa vazia! Tente novamente\n')
                interface()
                continue

            print('\nPeça selecionada: %s na casa %s\n' %(peca,pos_inicial))
            return peca, pos_inic

        except ValueError:
            print('\nValor em padrão incorreto! Tente novamente %s \n' % player)
            interface()
            continue

        except IndexError:
            print('\nValor fora do tabuleiro! Tente novamente %s \n' % player)
            interface()

#FUNÇÃO PARA RECEBER O DESTINO DA PEÇA QUE O USUÁRIO SELECIONOU
def seleciona_dest():
    '''Seleciona o destino da peça'''
    while True:

        try:
            pos_destinal = input(
                '%s, selecione o destino da peça no seguinte padrão: %s%s\n' % (player, letras[randint(0,7)],randint(0,7))).lower()
            pos_dest = ['', '']
            pos_dest[0] = letras.index(pos_destinal[0])
            pos_dest[1] = int(pos_destinal[1]) - 1
            dest = tab[pos_dest[1]][pos_dest[0]]

            return dest, pos_dest

        except ValueError:
            print('\n Valor em padrão incorreto! Tente novamente %s \n' % player)
            continue

        except IndexError:
            print('\n Valor fora do tabuleiro! Tente novamente %s \n' % player)
            continue

#FUNÇÃO QUE RECEBE O DESTINO DA PEÇA, E SE FOR VÁLIDO, REALIZA O MOVIMENTO
def movimento(pos_inic, pos_dest, peca, dest, w_move, b_move):
    '''Determina que função de movimentação deve ser usada'''
    if peca.endswith('T') and dest.endswith('K') or peca.endswith('K') and dest.endswith('T'):
        condicoes_roque(pos_inic, peca, w_move, b_move)

    if (peca == 'bK' and dest == 'bT') or (peca == 'wK' and dest == 'wT') or (
                    peca == 'bT' and dest == 'bK') or (peca == 'wT' and dest == 'wK'):
        roque(peca,dest,pos_dest,pos_inic)
    if peca.startswith('w') and dest.startswith('w') or peca.startswith('b') and dest.startswith('b'):
        print('\nVocê não pode capturar suas próprias peças!\n')
        return False
    if peca.endswith('P'):
        return peao(pos_inic, pos_dest, peca, dest)
    if peca.endswith('K'):
        return rei(pos_inic, pos_dest)
    if peca.endswith('H'):
        return cavalo(pos_inic, pos_dest)
    if peca.endswith('T'):
        return torre(pos_inic, pos_dest)
    if peca.endswith('B'):
        return bispo(pos_inic, pos_dest)
    if peca.endswith('Q'):
        return rainha(pos_inic, pos_dest, tab)

#FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DO REI
def rei(pos_inic, pos_dest):
    '''Valida o movimento do rei'''
    if abs(pos_dest[0] - pos_inic[0]) == 1 and abs(pos_dest[1] - pos_inic[1]) == 1:
        return True
    elif (abs(pos_dest[0] - pos_inic[0]) == 1 and pos_dest[1] == pos_inic[1]) or (
                    abs(pos_dest[1] - pos_inic[1]) == 1 and pos_dest[0] == pos_inic[0]):
        return True

    else:
        print('\nJogada inválida, o rei só move uma casa em qualquer direção')
        return False

#FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DA RAINHA
def rainha(pos_inic, pos_dest, tab):
    '''Valida o movimento das Rainhas'''

    if pos_dest[0] == pos_inic[0] and pos_dest[1] != pos_inic[1]:
        if pos_dest[1] > pos_inic[1]:
            for i in range(pos_inic[1] + 1, pos_dest[1]):
                if tab[i][pos_inic[0]] != '  ':
                    print('\nJogada inválida', tab[i][pos_inic[0]], 'no caminho\n')
                    return False
            return True

        elif pos_dest[1] < pos_inic[1]:
            for i in range(pos_inic[1] - 1, pos_dest[1], -1):
                if tab[i][pos_inic[0]] != '  ':
                    print('\nJogada inválida', tab[i][pos_inic[0]], 'no caminho\n')
                    return False
            return True

    if pos_dest[1] == pos_inic[1] and pos_dest[0] != pos_inic[0]:

        if pos_dest[0] > pos_inic[0]:
            for i in range(pos_inic[0] + 1, pos_dest[0]):
                print(tab[pos_inic[1]][i])
                if tab[pos_inic[1]][i] != '  ':
                    print('\nJogada inválida', tab[pos_inic[1]][i], 'no caminho\n')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0]:
            for i in range(pos_inic[0] - 1, pos_dest[0], -1):
                print(tab[pos_inic[1]][i])
                if tab[pos_inic[1]][i] != '  ':
                    print('\nJogada inválida', tab[pos_inic[1]][i], 'no caminho\n')
                    return False
            return True

    if abs(pos_dest[0] - pos_inic[0]) == abs(pos_dest[1] - pos_inic[1]):
        if pos_dest[0] > pos_inic[0] and pos_dest[1] > pos_inic[1]:  # inferior-direita
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] + i][pos_inic[0] + i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] + i][pos_inic[0] + i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] > pos_inic[0] and pos_dest[1] < pos_inic[1]:  # superior-direita
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] - i][pos_inic[0] + i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] - i][pos_inic[0] + i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0] and pos_dest[1] > pos_inic[1]:  # inferior-esquerda
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] + i][pos_inic[0] - i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] + i][pos_inic[0] - i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0] and pos_dest[1] < pos_inic[1]:  # superior-esquerda
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] - i][pos_inic[0] - i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] - i][pos_inic[0] - i], 'no caminho.\n')
                    return False
            return True

    else:
        return False

#FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DO PEAO
def peao(pos_inic, pos_dest, peca, dest):
    '''Função que valida o movimento dos peões'''

    if pos_dest[0] == pos_inic[0]:  # se a coluna for a mesma
        if (pos_inic[1] == 1 and peca.startswith('w')) or (
                    peca.startswith('b') and pos_inic[1] == 6):  # se o peão tá nas casas iniciais
            if abs(pos_dest[1] - pos_inic[1]) > 2:  # pode se mover até 2 casas
                print('\nNo primeiro movimento o peão só pode andar até 2 casas!\n')
                return False
            else:
                return True

        elif pos_inic[1] > 1 and peca.startswith('w'):
            if pos_dest[1] - pos_inic[1] > 1:
                print('\nO peão só pode andar 1 casa após o primeiro movimento!\n')
                return False
            elif dest != '  ':
                print('\nTem uma peça na posição\n')
                return False
            elif pos_dest[1] < pos_inic[1]:
                print('\nPeões não andam para trás!\n')
                return False
            else:
                return True

        elif (peca.startswith('b') and pos_inic[1] < 6):
            if pos_dest[1] - pos_inic[1] < -1:
                print('\nO peão só pode andar 1 casa após o primeiro movimento!\n')
                return False
            elif dest != '  ':
                print('\nTem uma peça na posição\n')
                return False
            elif pos_dest[1] > pos_inic[1]:
                print('\nPeões não andam para trás!\n')
                return False
            else:
                return True

    elif pos_dest[0] != pos_inic[0]:  # se tenta ir pra uma coluna diferente
        if pos_dest[1] == pos_inic[1]:
            print('\nO peão não pode andar de lado!\n')
            return False

        if peca.startswith('w') and dest.startswith('b'):
            if (pos_dest[0] == pos_inic[0] + 1 and pos_dest[1] == pos_inic[1] + 1) or (
                            pos_dest[0] == pos_inic[0] - 1 and pos_dest[1] == pos_inic[1] + 1):
                return True

        elif peca.startswith('b') and dest.startswith('w'):
            if (pos_dest[0] == pos_inic[0] + 1 and pos_dest[1] == pos_inic[1] - 1) or (
                            pos_dest[0] == pos_inic[0] - 1 and pos_dest[1] == pos_inic[1] - 1):
                return True

        else:
            print('\nO peão não pode andar de lado!\n')
            return False

    else:
        print('\nO peão não pode andar de lado!\n')
        return False

#FUNÇÃO QUE REALIZA A PROMOÇÃO DO PEÃO E OFERECE AS PEÇAS DISPONÍVEIS
def promocao(peca, tab, pos_dest):
    '''Função que promove o peão'''
    opcoesB = ['bT', 'bH', 'bB', 'bQ']
    opcoesW = ['wT', 'wH', 'wB', 'wQ']

    if peca == 'bP' and pos_dest[1] == 0:
        while True:
            try:
                escolha = int(input(
                    'O peão será promovido, escolha a peça que ele se tornará:\n1 = Torre\n2 = Cavalo\n3 = Bispo\n4 = Rainha\n- ')) - 1
                tab[pos_dest[1]][pos_dest[0]] = opcoesB[escolha]
                break
            except ValueError:
                print('Digite um valor inteiro')
                continue
            except IndexError:
                print('Valor não está nas opções, seleciona uma das peças')
                continue
        interface()

    elif peca == 'wP' and pos_dest[1] == 7:
        while True:
            try:
                escolha = int(input(
                    'O peão será promovido, escolha a peça que ele se tornará:\n1 = Torre\n2 = Cavalo\n3 = Bispo\n4 = Rainha\n- ')) - 1
                tab[pos_dest[1]][pos_dest[0]] = opcoesW[escolha]
                break
            except ValueError:
                print('Digite um valor inteiro')
                continue
            except IndexError:
                print('Valor não está nas opções, seleciona uma das peças')
                continue
        interface()

    return

#FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DA TORRE
def torre(pos_inic, pos_dest):
    #Valida o movimento da torre

    if pos_inic[0] != pos_dest[0] and pos_inic[1] != pos_dest[1]:
        print('Movimento inválido. Tente andar na mesma linha e coluna diferente ou mesma coluna e linha diferente')
        return False

    if pos_dest[0] == pos_inic[0] and pos_dest[1] != pos_inic[1]:

        if pos_dest[1] > pos_inic[1]:  # pra direita
            for i in range(pos_inic[1] + 1, pos_dest[1]):
                if tab[i][pos_inic[0]] != '  ':
                    print('Jogada inválida', tab[i][pos_inic[0]], 'no caminho')
                    return False
            return True

        elif pos_dest[1] < pos_inic[1]:  # pra esquerda
            for i in range(pos_inic[1] - 1, pos_dest[1], -1):
                if tab[i][pos_inic[0]] != '  ':
                    print('Jogada inválida', tab[i][pos_inic[0]], 'no caminho')
                    return False
            return True

    if pos_dest[1] == pos_inic[1] and pos_dest[0] != pos_inic[0]:

        if pos_dest[0] > pos_inic[0]:  # pra baixo
            for i in range(pos_inic[0] + 1, pos_dest[0]):
                if tab[pos_inic[1]][i] != '  ':
                    print('Jogada inválida', tab[pos_inic[1]][i], 'no caminho')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0]:  # pra cima
            for i in range(pos_inic[0] - 1, pos_dest[0], -1):
                if tab[pos_inic[1]][i] != '  ':
                    print('Jogada inválida', tab[pos_inic[1]][i], 'no caminho')
                    return False
            return True

    else:
        return True

#FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DO CAVALO
def cavalo(pos_inic, pos_dest):
    '''Valida o movimento do cavalo'''
    if abs(pos_dest[0] - pos_inic[0]) == 2 and abs(pos_dest[1] - pos_inic[1]) == 1:
        return True
    elif abs(pos_dest[0] - pos_inic[0]) == 1 and abs(pos_dest[1] - pos_inic[1]) == 2:
        return True
    else:
        print(
            "Jogada Inválida! \nO cavalo só pode se mover em um movimento em formato de L "
            "(2 colunas + 1 linha ou 1 coluna + 2 linhas")
        return False

##FUNÇÃO DE MOVIMENTAÇÃO E CONDIÇÕES DO BISPO
def bispo(pos_inic, pos_dest):
    '''Valida o movimento dos bispos'''

    if abs(pos_dest[0] - pos_inic[0]) == abs(pos_dest[1] - pos_inic[1]):
        if pos_dest[0] > pos_inic[0] and pos_dest[1] > pos_inic[1]:  # inferior-direita
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] + i][pos_inic[0] + i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] + i][pos_inic[0] + i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] > pos_inic[0] and pos_dest[1] < pos_inic[1]:  # superior-direita
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] - i][pos_inic[0] + i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] - i][pos_inic[0] + i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0] and pos_dest[1] > pos_inic[1]:  # inferior-esquerda
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] + i][pos_inic[0] - i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] + i][pos_inic[0] - i], 'no caminho.\n')
                    return False
            return True

        elif pos_dest[0] < pos_inic[0] and pos_dest[1] < pos_inic[1]:  # superior-esquerda
            for i in range(1, abs(pos_dest[0] - pos_inic[0])):
                if tab[pos_inic[1] - i][pos_inic[0] - i] != '  ':
                    print('\nJogada inválida, ', tab[pos_inic[1] - i][pos_inic[0] - i], 'no caminho.\n')
                    return False
            return True

    else:
        print('Jogada inválida')
        return False

#FUNÇÃO DA CAPTURA DE PEÇAS
def captura(peca, pos_inic, pos_dest):
    '''Captura uma peça, substituindo nas posições'''
    tab[pos_dest[1]][pos_dest[0]] = peca
    tab[pos_inic[1]][pos_inic[0]] = '  '

#FUNÇÃO QUE DETERMINA O FIM DO JOGO E MOSTRA O VENCEDOR
def xeque_mate(dest):
    '''Realiza o xeque-mate'''
    if ((dest == 'bK' and player == player1) or (dest == 'wK' and player == player2)):
        print('   \n      ♚ Parabéns %s, você venceu! ♚ \n' % player)
        print('   XEQUE-MATE! Você capturou o Rei inimigo!\n')
        print('         ♚ Obrigado por jogar! ♚      \n')
        while True:
            resposta = input('\nQuerem jogar novamente? (S/N)').upper()
            if resposta == 'S':
                main()
            elif resposta == 'N':
                print('\nJogo encerrado!')
                quit()
            else:
                print('Resposta inválida')
                continue

#FUNÇÃO QUE REALIZA A JOGADA DO ROQUE (INCOMPLETO)
def roque(peca, dest, pos_dest, pos_inic):
    hold = [peca,dest]
    if pos_dest[1] > pos_inic[1]:  # pra direita
        for i in range(pos_inic[1] + 1, pos_dest[1]):
            if tab[i][pos_inic[0]] != '  ':
                print('Roque inválido', tab[i][pos_inic[0]], 'no caminho')
                return False

        peca = hold[1]
        dest = hold[0]

        return True, peca, dest

    elif pos_dest[1] < pos_inic[1]:  # pra esquerda
        for i in range(pos_inic[1] - 1, pos_dest[1], -1):
            if tab[i][pos_inic[0]] != '  ':
                print('Roque inválido', tab[i][pos_inic[0]], 'no caminho')
                return False

        peca = hold[1]
        dest = hold[0]

        return True, peca, dest

#FUNÇÃO QUE DEFINE AS CONDIÇÕES PARA A REALIAÇÃO DO ROQUE (INCOMPLETO)
def condicoes_roque(pos_inic,peca,w_move,b_move):
    '''Condições pro Roque'''

    if peca == 'wK' and w_move[0] == False:
        w_move[0] = True

    if peca == 'wT':
        if pos_inic == [0, 0] and w_move[1] == False:
            w_move[1] = True
        if pos_inic == [7, 0] and w_move[2] == False:
            w_move[2] = True

    if peca == 'bK' and b_move[0] == False:
        b_move[0] = True

    if peca == 'bT':
        if pos_inic == [0, 7] and b_move[1] == False:
            b_move[1] = True
        if pos_inic == [7, 7] and b_move[2] == False:
            b_move[2] = True

    return w_move, b_move

#FUNÇÃO PRINCIPAL DO JOGO E QUE O ORGANIZA
def main():
    '''Função central do jogo, que chama as demais e define as variáveis'''
    global tab, letras, player, player1, player2

    tab = [['wT', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wT'],
           ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
           ['bT', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bT']]

    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # para trocar os valores das letras digitadas por números

    player1, player2 = (nomes_jogadores())  # define os nomes
    player = player1  # quem joga primeiro
    w_move = [False, False, False]
    b_move = [False, False, False]

    contador_erros = 0
    jogadavalida = False
    interface()

    while jogadavalida == False:
        if contador_erros == 3:  # se o player errar o input 3x o tabuleiro é reimpresso
            interface()
            contador_erros = 0
        try:
            peca, pos_inic = seleciona_peca()
            dest, pos_dest = seleciona_dest()
            jogadavalida = movimento(pos_inic, pos_dest, peca, dest, w_move, b_move)

            if jogadavalida == True:
                captura(peca, pos_inic, pos_dest)          #se a jogada valeu, coloca a peça no lugar indicado
                interface()
                promocao(peca, tab, pos_dest)
                print('\n    O movimento escolhido é válido!\n')
                print('         Movimento realizado ✔\n')
                xeque_mate(dest)                           #dá o xeque-mate caso o rei tenha sido comido
                contador_erros = 0

                '''Troca de turnos'''

                if player == player1:
                    player = player2
                    jogadavalida = False
                    continue
                else:
                    player = player1
                    jogadavalida = False
                    continue
            else:
                contador_erros += 1

        except IndexError:
            print('Valor fora do tabuleiro, tente novamente!')
            interface()
            contador_erros += 1
            continue


while True:
    '''Loop da tela inicial'''
    opcao = input(
        "\n\nEscolha uma opção:\n(1)Começar a partida\n(2)Ler instruções do DDMChess\n(3)Ler regras de movimentação do Xadrez\n - ")
    if opcao == '1':
        print('\n3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('\nGo!\n')
        main()
        break

    elif opcao == '2':
        print('                       As peças são representadas por 2 letras.'
              '\n                       A primeira é minúscula e indica a cor da peça:'
              '\n                         - w = brancas (white)'
              '\n                         - b = pretas (black)\n'
              '\n                       A segunda letra, é maiúscula e indica o tipo de peça:'
              '\n                         - K = Rei (King)'
              '\n                         - Q = Rainha (Queen)'
              '\n                         - T = Torre (Tower)'
              '\n                         - B = Bispo (Bishop)'
              '\n                         - H = Cavalo (Horse)'
              '\n                         - P = Peão (Pawn)\n'
              '\n                       O jogo é multiplayer para 2 jogadores locais!\n')
        continue

    elif opcao == '3':
        print('                             REGRAS DO XADREZ                \n')
        print('TORRE (wT ou bT) :Se movimenta para frente e para trás, para direita e para esquerda\n'
              '                  mas não pode pular nenhuma outra peça.\n'
              'BISPO (wB ou bB) :Se movimenta na diagonal mantendo-se sempre nas casas\n'
              '                  de mesma cor que se encontrava no início do jogo, podendo\n'
              '                  ir para frente e para trás quantas casas quiser, mas não pode pular\n'
              '                  nenhuma outra peça.\n'
              'CAVALO (wH ou bH):Se movimenta em formato de ''L''O cavalo se movimenta 2 casas para\n'
              '                  frente ou para trás e em seguida 1 casa para a direita ou para a\n'
              '                  esquerda, ou 2 casas para a direita ou para a esquerda e em seguida 1\n'
              '                  casa para frente ou para trás. O cavalo é a única peça do xadrez que\n'
              '                  pode pular outras peças.\n'
              'RAINHA (wQ ou bQ):Se movimenta para frente ou para trás, para direita ou para esquerda,\n'
              '                  ou na diagonal, quantas casas quiser, mas não pode pular nenhuma outra.\n'
              'REI (wK ou bK)   :Se movimenta apenas 1 casa em qualquer direção. O rei nunca pode se\n'
              '                  movimentar para uma casa que esteja sob ataque ou capturar uma peça que\n'
              '                  esteja defendida por uma peça adversária.\n'
              'PEÃO (wP ou bP)  :Se movimenta apenas para frente sendo a única peça que não se move\n'
              '                  para trás. No primeiro lance de cada peão ele pode avançar 1 ou 2 casas.\n'
              '                  A partir do segundo lance, ele só poderá mover-se apenas 1 casa.\n')
    else:
        print("Digite um valor válido!")
        continue

'''
Faltam:

Xeque
Roque

'''
