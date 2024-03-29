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

    # SENTENÇA - INICIO
    sentencas = separa_sentencas(texto)
    total_sentencas = len(sentencas)

    caracteres_sentenca = 0
    for i in range(total_sentencas):
        caracteres_sentenca += len(sentencas[i])
    # SENTENÇA - FIM

    # FRASES - INICIO
    frases = []
    ## Para cada frase encontrado dentro do range "sentenças", ela será incluida na lista 'frases'.
    for fr in range(len(sentencas)):
        frases_sentencas = separa_frases(sentencas[fr])
        for f in range(len(frases_sentencas)):
            frases.append(frases_sentencas[f])

    total_frases_sentenca = len(frases)

    caracteres_frases = 0
    for i in range(total_frases_sentenca):
        caracteres_frases += len(frases[i])

    # FRASES - FIM

    # PALAVRAS - INICIO
    ## Para cada palavras encontrado dentro do range "frases", ela será incluida na lista 'palavras'.
    palavras = []
    for pl in range(len(frases)):
        palavras_sentencas = separa_palavras(frases[pl])
        for p in range(len(palavras_sentencas)):
            palavras.append(palavras_sentencas[p])

    total_palavras_texto = len(palavras)

    ## Calcular todos os caracteres dentro da lista 'palavras'
    n_caracteres_palavras = 0
    for c in range(len(palavras)):
        n_caracteres_palavras += len(palavras[c])

    ## Irá buscar as palavras diferentes dentro da lista 'palavras'
    diferentes = n_palavras_diferentes(palavras)

    ## Irá buscar as palavras unicas dentro da lista 'palavras'
    unicas = n_palavras_unicas(palavras)

    # PALAVRAS - FIM

    media_palavras = n_caracteres_palavras / total_palavras_texto # Todos os caracteres / Todas as palavras do texto
    relacao_type_token = diferentes/total_palavras_texto # Palavras diferentes no texto / Todas as palavras
    hapax_legomana = unicas/total_palavras_texto # Palavras únicas no texto / Todas as palavras
    tamanho_media_sentencas = caracteres_sentenca / total_sentencas # Todos os caracteres / Todas as sentenças no texto

    complexidade_media_sentenca = total_frases_sentenca / total_sentencas # Todas as frases / Todas as sentenças
    tamanho_medio_frases = caracteres_frases / total_frases_sentenca # Todos os caracteres / Todas as frases

    assinatura = [media_palavras,relacao_type_token,hapax_legomana,tamanho_media_sentencas,
                  complexidade_media_sentenca,tamanho_medio_frases]

    return assinatura


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
    e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''

    # COMPARA OS TEXTOS E DEFINE O GRAU DE SIMILARIDADE DE CADA UM
    total_textos = len(textos)
    grau_similaridade = []
    for t in range(total_textos):
        ass_texto = calcula_assinatura(textos[t])
        similaridade = compara_assinatura(ass_texto, ass_cp)
        grau_similaridade.append(similaridade)

    # A SIMILARIDADE VAI DEFINIR O MENOR NÍVEL DE PROXIMIDADE DOS TEXTOS

    i = 1
    menor_nivel = grau_similaridade[0] #Pega o grau de similaridade da primeira posição
    infectado = i #texto infectado vai ser igual a i

    while i < len(grau_similaridade): #enquanto o valor de i for menor que o comprimento de similaridades da lista
        if grau_similaridade[i] < menor_nivel: # Se o grau de similaridade for menor que o menor_nivel:
            menor_nivel = grau_similaridade[i] # O menor nivel vai pegar o grau de similaridade daquela posição
            infectado = (i+1)
        i += 1

    print(f"O autor do texto {infectado} está infectado com COH-PIAH")
    return infectado