import re
import string


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    # Sab = ((Somatorio) No intervalo de i = 1 e máximo 6 | F i,a - F i,b) / 6
    Sab = 0
    for i in range (0,6):
        Sab += (abs(as_a[i] - as_b[i]))

    similaridade = Sab/6

    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    # SEPARA AS PALAVRAS DO TEXTO E GUARDA NA VARIÁVEL
    palavras = separa_palavras(texto)

    # Remove a pontuação e espaços das strings no texto
    palavras_texto = [''.join(c for c in s if c not in string.punctuation) for s in palavras]
    # SOMA O TOTAL DE PALAVRAS NO TEXTO, SEM A PONTUAÇÃO
    total_palavras_texto = len(palavras_texto)

    # SEPARA OS CARACTERES DAS PALAVRAS E SOMA O TOTAL DELAS
    n_caracteres = 0
    for i in range(total_palavras_texto):
        n_caracteres += len(palavras_texto[i])

    # VAI USAR A FUNÇÃO "PALAVRAS DIFERENTES" PARA CALCULAR AS "PALAVRAS DO TEXTO" DEFINIDAS ANTES
    diferentes = n_palavras_diferentes(palavras_texto)

    # VAI USAR A FUNÇÃO "PALAVRAS UNICAS" PARA CALCULAR AS "PALAVRAS DO TEXTO" DEFINIDAS ANTES
    unicas = n_palavras_unicas(palavras_texto)

    # SEPARA AS SENTENÇAS DO TEXTO, E SOMA O TOTAL DELAS
    sentencas = separa_sentencas(texto)
    total_sentencas = len(sentencas)

    # CONTA TODOS OS CARACTERES DA SENTENÇA. É DIFERENTE DOS CARACTERES CALCULADOS ANTES

    # string.punctuation remove a pontuação, o calculo dos caracteres irá desconsiderar eles
    sent_caracteres = [''.join(c for c in s if c not in string.punctuation) for s in sentencas]
    caracteres_sem_pontuacao = 0

    caracteres_sentenca = 0
    for i in range(total_sentencas):
        caracteres_sentenca += len(sentencas[i])
        caracteres_sem_pontuacao += len(sent_caracteres[i])  # sent_caracteres são as sentenças sem pontuação

    # SEPARA AS FRASES DA SENTENÇA
    total_frases_sentenca = 0
    for sentenca in sentencas:
        total_frases_sentenca += len(separa_frases(sentenca))


    media_palavras = n_caracteres / total_palavras_texto # Todos os caracteres / Todas as palavras do texto
    relacao_type_token = diferentes/total_palavras_texto # Palavras diferentes no texto / Todas as palavras
    hapax_legomana = unicas/total_palavras_texto # Palavras únicas no texto / Todas as palavras
    tamanho_media_sentencas = caracteres_sentenca / total_sentencas # Todos os caracteres / Todas as sentenças no texto

    complexidade_media_sentenca = total_frases_sentenca / total_sentencas # Todas as frases / Todas as sentenças
    tamanho_medio_frases = caracteres_sem_pontuacao / total_frases_sentenca # Todos os caracteres / Todas as frases

    assinatura = [media_palavras,relacao_type_token,hapax_legomana,tamanho_media_sentencas,
                  complexidade_media_sentenca,tamanho_medio_frases]
    print(assinatura)
    return assinatura


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
    e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''

    i = 1
    # ASS_TEXTO = TEXTO DIGITADO | SIMILARIDADE = VAI COMPARAR O TEXTO DIGITADO COM OS VALORES PADRÕES
    ass_texto = calcula_assinatura(textos[i])
    similaridade = compara_assinatura(ass_texto, ass_cp)

    # A SIMILARIDADE VAI DEFINIR O MENOR NÍVEL DE PROXIMIDADE DOS TEXTOS
    menor = similaridade


    texto_copiado = i
    i += 1
    while i < (len(textos)):
        ass_texto = calcula_assinatura(textos[i])
        similaridade = compara_assinatura(ass_texto, ass_cp)
        if similaridade < menor:
            menor = similaridade
            texto_copiado = i
        i = i + 1

    print(f"O autor do texto {texto_copiado} está infectado com COH-PIAH")
    return texto_copiado
