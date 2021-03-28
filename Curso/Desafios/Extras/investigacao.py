# Um assassinato aconteceu, e o programa fará 5 perguntas para o usuário.
# Se 2 respostas forem positivas, o usuário é considerado: "SUSPEITO"
# Se responder entre 3 e 4 respostas positivas: "CÚMPLICE"
# 5 respostas positivas, o usuário é considerado como: "ASSASSINO"
# Caso o usuário tenha no máximo 1 resposta positiva, ele é: "INOCENTE"

# Uma função para chamar as perguntas
def perguntas(res, tel, loc, mor, div, tra):
    tel = res.append(telefone(tel))
    loc = res.append(local(loc))
    mor = res.append(morada(mor))
    div = res.append(divida(div))
    tra = res.append(trabalho(tra))

    return res, tel, loc, mor, div, tra

# Pergunta sobre telefonema
def telefone(tel):
    tel = input('Telefonou para a vítima? ').lower().strip()

    if tel != 'sim' and tel != 'não' and tel != 'nao':
        print('Por favor, responda apenas com sim ou não.')
        telefone(tel)

    return tel

# Pergunta sobre localização durante o crime
def local(loc):
    loc = input('Esteve no local do crime? ').lower().strip()

    if loc != 'sim' and loc != 'não' and loc != 'nao':
        print('Por favor, responda apenas com sim ou não.')
        local(loc)

    return loc

# Pergunta sobre morada do suspeito
def morada(mor):
    mor = input('Mora perto da vítima? ').lower().strip()

    if mor != 'sim' and mor != 'não' and mor != 'nao':
        print('Por favor, responda apenas com sim ou não.')
        morada(mor)

    return mor

# Pergunta sobre divida
def divida(div):
    div = input('Devia para a vítima? ').lower().strip()

    if div != 'sim' and div != 'não' and div != 'nao':
        print('Por favor, responda apenas com sim ou não.')
        divida(div)

    return div

# Pergunta sobre trabalho do usuário
def trabalho(tra):
    tra = input('Já trabalhou com a vítima? ').lower().strip()

    if tra != 'sim' and tra != 'não' and tra != 'nao':
        print('Por favor, responda apenas com sim ou não.')
        trabalho(tra)

    return tra


# Função para pegar as repostas e adiciona-las numa lista
def respostas(nome,sexo):
    res = []

    tel = ''
    loc = ''
    mor = ''
    div = ''
    tra = ''
    perguntas(res, tel, loc, mor, div, tra)

    # O programa vai somar quantas respostas SIM e NÃO tiveram
    sim = res.count('sim')
    nao = res.count('não') + res.count('nao') # O não é somado se o usuário colocar ou não acento

    # Analise das respostas 'SIM' e resultado para o usuário
    # Quando o usuário colocar o SEXO como HOMEM, as respostas serão para o sexo masculino
    # Se o usuário colocar MULHER, as respostas serão no gênero feminino.
    if sim <= 1 and sexo == 'homem':
        print('\n{}, você foi considerado inocente'.format(nome))
    if sim <= 1 and sexo == 'mulher':
        print('\n{}, você foi considerada inocente'.format(nome))

    if sim == 2 and sexo == 'homem':
        print('\n{}, você é um suspeito'.format(nome))
    if sim == 2 and sexo == 'mulher':
        print('\n{}, você é uma suspeita'.format(nome))

    if sim > 2 and sim <= 4:
        print('\n{}, você é cúmplice do crime!'.format(nome))

    if sim == 5 and sexo == 'homem':
        print('\n{}, você será detido por assassinato!'.format(nome))
    if sim == 5 and sexo == 'mulher':
        print('\n{}, você será detida por assassinato!'.format(nome))


# Introdução do programa
def main():
    print('Olá, obrigado pela sua presença.')

    nome = input('Para começar, qual o seu nome? ').strip()

    sexo = input('Você é homem ou mulher? ').lower().strip()
    if sexo != 'homem' and sexo != 'mulher':
        print('Não entendi. Vou tratar você como homem')
        sexo = 'homem'

    print('\nO{}, por gentileza, durante as perguntas responda apenas com \033[1mSim\033[m ou \033[1mNão\033[m'.format(nome))

    comeco = input('\nPodemos começar? Responda com Sim ou Não: ').lower().strip()
    if comeco == 'sim':
        print('')
        respostas(nome,sexo)
    else:
        print('Desculpa, mas não podemos demorar. Vamos ter que continuar assim mesmo')
        print('')
        respostas(nome,sexo)

    return nome,sexo

main()