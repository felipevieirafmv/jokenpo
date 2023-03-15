import random

def esc_jogador():
    while True:
        escjogadorstr = input('1- Pedra\n2- Papel\n3- Tesoura\nDigite "0" para sair\nEscolha: ')
        if escjogadorstr == 'The Rock':
            escjogador = 'The Rock'
            break
        else:
            escjogador = int(escjogadorstr)
        if escjogador == 1:
            escjogador = 'Pedra'
            break
        elif escjogador == 2:
            escjogador = 'Papel'
            break
        elif escjogador== 3:
            escjogador = 'Tesoura'
            break
        elif escjogador == 0:
            print('Jogo encerrado.')
            break
        else:
            print('Opção inválida')
            
    return escjogador
        
def jog_jogador():
    escjogador = esc_jogador()
    if escjogador == 'Pedra':
        jogjogador = '''    ____
  _/  _ \\
 / _ - _ \\
 \\_______/   

'''
    elif escjogador == 'Papel':
        jogjogador = '''   _____
  O_____O
  /     /
 /____ /
O_____O

'''
    elif escjogador == 'Tesoura':
        jogjogador = '''    _    _
   (_)  / )
     | (_/ 
    _+/  
   //|\\
  // ||
 (/  |/ 

'''
    else:
        jogjogador = None
    return jogjogador, escjogador

def esc_maquina():
    escmaquina = random.randint(1, 3)
    if escmaquina == 1:
        escmaquina = 'Pedra'
    elif escmaquina == 2:
        escmaquina = 'Papel'
    elif escmaquina == 3:
        escmaquina = 'Tesoura'
    return escmaquina

def jogada_maquina():
    escmaquina = esc_maquina()
    if escmaquina == 'Pedra':
        jogmaquina = '''   ____
  _/  _ \\
 / _ - _ \\
 \\_______/   

'''
    elif escmaquina == 'Papel':
        jogmaquina = '''  _____
  O_____O
  /     /
 /____ /
O_____O

'''
    elif escmaquina == 'Tesoura':
        jogmaquina = '''   _    _
   (_)  / )
     | (_/ 
    _+/  
   //|\\
  // ||
 (/  |/ 

'''
    return jogmaquina, escmaquina

def verificacao():
     # escjogador = esc_jogador()
    # escmaquina = esc_maquina()
    vit = 0
    der = 0
    cont = 0
    while True:
        jogmaquina, escmaquina = jogada_maquina()
        jogjogador, escjogador = jog_jogador()
        if escjogador == escmaquina:
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nEmpatou.')
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            cont += 1
            print('-'*68)
        elif escjogador == 'Pedra' and escmaquina == 'Papel':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nPapel ganha de pedra.\nVocê perdeu!')
            der += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'Pedra' and escmaquina == 'Tesoura':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nPedra ganha de tesoura.\nVocê ganhou!')
            vit += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'Papel' and escmaquina == 'Pedra':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nPapel ganha de pedra.\nVocê ganhou!')
            vit += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'Papel' and escmaquina == 'Tesoura':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nTesoura ganha de papel.\nVocê perdeu!')
            der += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'Tesoura' and escmaquina == 'Pedra':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nPedra ganha de tesoura.\nVocê perdeu!')
            der += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'Tesoura' and escmaquina == 'Papel':
            print(f'Você escolheu:\n{jogjogador}O computador escolheu:\n {jogmaquina}\nTesoura ganha de papel.\nVocê ganhou!') 
            vit += 1
            cont += 1
            print(f'\nSua pontuação atual: {vit}\nPontuação atual da máquina: {der}\n')
            print('-'*68)
        elif escjogador == 'The Rock':
            print('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
        elif escjogador == 0:
            break
    return vit, der, cont

def jogar():
    cont = 0
    condicao = True
    print('Bem vindo ao jogo :)')
    while condicao == True:
        try:
            if cont == 0:
                soun = int(input('Deseja começar o jogo? 1- Sim. 2- Não\nR: '))
                if soun == 2:
                    cont += 1
                    condicao = False
                    break
                elif soun == 1 :
                    verificacao()
                    condicao = False
                else:
                    print('Opção inválida')
        except KeyboardInterrupt:
            print('\nPrograma encerrado pelo usuário.')
            break
        except ValueError:
            print('\nValor inválido.')
        except:
            print('Erro')
            break
    
jogar()