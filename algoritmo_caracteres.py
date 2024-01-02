import os

comprimido = []                            #lista que vai armazenar o texto comprimido
descomprimido = []                         #lista que vai armazenar o texto descomprimido

# COMPRESSÃO
with open("repeticao_caracteres.txt", "r") as arquivo: #abre o arquivo original
    texto = arquivo.read()                          #le o arquivo, armazena na var texto e fecha arq

caracteres = list(texto)                   #var caracteres armazena o texto em lista, assim podemos manipular cada caractere individualmente

tamanho = len(caracteres)-1                #-1 pq vamos comparar a iteração ao índice da lista, que começa com 0, ñ 1
i = 0                                      #var da iteração

while i <= tamanho:                        #loop vai parar quando chegar no último item da lista
    caractere_atual = caracteres[i]         #a cada início de iteração, definimos o caractere_atual e resetamos a qnt_caract para 1
    qnt_caract = 1                       
    while i < tamanho and caracteres[i+1] == caractere_atual:   #até o penúltimo item, checamos se o próx. caractere é igual ao atual
        qnt_caract += 1                                              #se for, a var qnt_caract aumenta 1 e "pulamos" pro próximo caractere
        i += 1
    if qnt_caract > 4:                      #se a qnt_caract for maior que 4, adiciona à lista comprimido a flag (#), o multiplicador (qnt_caract) e o caractere repetido
        comprimido.append("#" + str(qnt_caract) + caractere_atual)
    elif caractere_atual.isdigit():         #se o caractere atual for um número, add um | antes do caractere
        comprimido.append("|" + caractere_atual)    
    else:                                   #se ñ for maior que 4 e nem for um numero, o caractere atual é multiplicado pela qnt de vezes q foi repetido e é add à lista comprimido
        comprimido.append(caractere_atual * qnt_caract)       
    i += 1                                  #ao final da iteração, add 1 para "pular" p/ próx.

comprimido = "".join(comprimido)           #junta os itens da lista (cada caractere) numa string

with open("comprimido.txt", "w") as arquivo_comprimido:  #cria o novo arquivo comprimido.txt
    texto_comprimido = arquivo_comprimido.write(comprimido) #escreve a lista comprimido no arquivo comprimido.txt e fecha arq


# DESCOMPRESSÃO
with open("comprimido.txt", "r") as arquivo_c:    #abre o arquivo comprimido
    texto_c = arquivo_c.read()                 #le o arquivo comprimido, armazena na var texto_c e fecha arq

caracteres = list(texto_c)                 #var caracteres armazena o texto_c em lista, assim podemos manipular cada caractere individualmente

caract_rep = ""

for i, caractere in enumerate(caracteres):      #loop vai percorrer a lista (caracteres), acompanhando o índice (i) e o valor do item (caractere)
    if caractere == "#":
        qnt_caract = ""                        #se o caractere atual for uma #, limpa a var qnt_caract, estamos numa nova seq
        while caracteres[i+1].isdigit():        #loop ocorre enquanto o próximo caractere for um dígito. isso serve para garantir que o multiplicador da flag será reconhecido, msm q seja maior q 9
            qnt_caract += caracteres[i+1]          #o caractere numérico é add à var qnt_caract e "pula" pro próx. caractere
            i += 1
        if qnt_caract:                         #checa se a var qnt_caract guarda um valor diferente de 0
            qnt_caract = int(qnt_caract)-1        #converte a var para int, subtraindo 1 (o próprio caractere da flag ñ será multiplicado)
            caract_rep = caracteres[i+1]            #var caract_rep armazena o caractere da flag
            descomprimido.append(caract_rep * qnt_caract)     #e multiplica esse número pelo caractere repetido, add à lista descomprimido
        else:
           descomprimido.append("#")            #se a var qnt_caract estiver vazia, a # encontrada é um caractere e ñ uma flag. ela é add à lista descomprimido                              
    elif caractere == "|" and caracteres[i+1].isdigit():  #se o caractere atual for uma |, sabemos que era um número no texto original
        descomprimido.append(caracteres[i+1])               #o número que procede a | é add à lista descomprimido
    elif not caractere.isdigit():
        descomprimido.append(caractere)         #se o caractere atual ñ for uma flag, ele é add à lista descomprimido

descomprimido = "".join(descomprimido)     #junta os itens da lista (cada caractere) numa string

with open("descomprimido.txt", "w") as arquivo_descomprimido: #cria o novo arquivo descomprimido.txt
    texto_descomprimido = arquivo_descomprimido.write(descomprimido) #escreve a lista descomprimido no arquivo descomprimido.txt e fecha arq