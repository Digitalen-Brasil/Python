# Programa para converter dados de texto usando condição if

print('\n\033[1;30;41mATENÇÃO!\033[m Responda com \033[1;4mSim\033[m ou \033[1;4mNão\033[m\n')

# Vai receber se o argumento se é final de semana sim ou não
findi = input('É final de semana? ')
fds = findi.strip().lower() # Converte a reposta para minúscula e remove todos os espaços

# Se for final de semana, resposta 'sim, vai executar essa ação:
if fds == 'sim':
    clima = input('Tem previsão de sol? ')
    sol = clima.strip().lower()

# Se a previsão de sol for 'sim' a frase positiva aparece
    if sol == 'sim':
        print('Então vamos a praia!')

# Se a previsão de sol for 'não' parece uma mensagem de negação.
    else:
        print('Provavelmente eu não vá então')

# Se não for final de semana:
elif fds == 'não':

# Vai receber o argumento se é feriado sim ou não
    feriado = input('É feriado? ')
    fer = feriado.strip().lower() # Converte para minúsculo e remove espaços

# Se for Feriado, vai executar essa ação:
    if fer == 'sim':
        clima = input('Tem previsão de sol? ')
        sol = clima.strip().lower()

# Se for fazer sol, encerra com mensagem positiva
        if sol == 'sim':
            print('Então vamos a praia!')

# Se não tiver previsão de sol, vai ter uma negativa.
        else:
            print('Provavelmente eu não vá então')

#Se não for final de semana e nem feriado:
    else:
        print('Então não vai dar pra ir pra praia')

# Mensagem de entrada errada nas respostas
if fds != 'sim' and fds != 'não':
    print('Por favor digite apenas sim ou não')




