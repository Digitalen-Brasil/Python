def campeonato():
    # Valores iniciais que serão somados durante as partidades de um campeonato
    jogos = 0 # Número de jogos
    rodada = 1 # Número das rodadas
    usuario = 0 # Pontos do usuário
    computador = 0 # Pontos do computador

    # Limite de 3 jogos. Contador inicia em 0
    while jogos < 3:
        print('\n**** Rodada {} ****'.format(rodada))
        vencedor = partida()
        jogos += 1
        rodada += 1
        if vencedor == 1:
            usuario += 1
        else:
            computador += 1

    print('\n**** Final do campeonato! ****')
    print('Placar: Você {} X {} Computador'.format(usuario, computador))


def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    usuario = 0
    computador = 0

    if (n % (m + 1) == 0):
        print('\nVocê começa!')
        jogada = 1 # Vez do usuário
    else:
        print('\nComputador começa!')
        jogada = 2 # Vez do Computador

    while n > 0:
        # Pega o retorno de N na escolha do usuário
        if jogada == 1:
            n = n - usuario_escolhe_jogada(n, m)
            jogada = 2
            if n > 1:
                print('Agora restam {} peças no tabuleiro'.format(n))
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n <= 0:
                print('Você ganhou!')
                return 1 # Retorna +1 ponto em Campeonato() para o usuário

        else:
            # Pega o retorno de N na escolha do comnputador
            n = n - computador_escolhe_jogada(n, m)
            jogada = 1
            if n > 1:
                print('Agora restam {} peças no tabuleiro'.format(n))
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n <= 0:
                print('Fim do jogo! O computador ganhou!')
                return 0 # Retorna +1 ponto em Campeonato() para o computador


def usuario_escolhe_jogada(n, m):
    # Regulamenta a jogada do USUARIO
    jogadaUsuario = input('\nQuantas peças você vai tirar? ')


    # Se o usuario tentar tirar mais peças que o limite
    if jogadaUsuario > m:
        print('Oops! Jogada inválida! Tente de novo.')
        return usuario_escolhe_jogada(n, m)

    # Se o usuario não mover peças ou tentar por número negativo
    if jogadaUsuario <= 0:
        print('Jogada Inválida. Tente novamente')
        return usuario_escolhe_jogada(n, m)

    while jogadaUsuario <= m:
        n = jogadaUsuario

        if jogadaUsuario == 1:
            print('\nVocê tirou uma peça.')
        else:
            print('\nVocê tirou {} peças.'.format(jogadaUsuario))
        break

    return n # Vai retornar o valor de N na jogada válida do usuário


def computador_escolhe_jogada(n, m):
    jogadaComputador = n % (m + 1) # Computador vai sempre testar a estratégia ideal

    # Se o valor ideal for igual ou superior ao limite, o computador vai jogar o limite
    if jogadaComputador == m or jogadaComputador > m:
        n = jogadaComputador = m
    else:
        n = jogadaComputador

    if jogadaComputador == 1:
        print('\nO computador tirou uma peça.')
    else:
        print('\nO computador tirou {} peças.'.format(jogadaComputador))

    return n # Retorna o valor de N da jogada ideal para o computador


def menu():
    escolha = int(input('\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

    # Escolha 1 vai levar para uma única partida
    if escolha == 1:
        print('\nVocê escolheu uma partida isolada!')
        partida()

    # Escolha 2 vai levar para 3 partidas, com rodadas e pontuação
    if escolha == 2:
        print('\nVocê escolheu um campeonato!')
        campeonato()

    # Qualquer valor diferente de 1 e 2 vai reiniciar o menu
    while escolha != 1 and escolha != 2:
        print('\nDesculpa, opção inválida. Tente novamente')
        menu()
        break

menu()