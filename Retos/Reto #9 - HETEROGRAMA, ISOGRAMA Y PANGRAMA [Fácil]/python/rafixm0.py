
# Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA:
#   Crea 3 funciones, cada una encargada de detectar si una cadena de
#   texto es un heterograma, un isograma o un pangrama.
#   Debes buscar la definición de cada uno de estos términos.

#   Pangrama: es un texto que usa todas las letras posibles del alfabeto de un idioma. 
#   Heterograma: es una palabra o frase que no contiene ninguna letra repetida
#   Isograma: es una palabra o frase en la que cada letra aparece el mismo número de veces.


def normalizar_cadena(texto):
    texto = texto.lower()

    reemplazos = (
        ('á', 'a'),
        ('é', 'e'),
        ('í', 'i'),
        ('ó', 'o'),
        ('ú', 'u'))
    
    for a, b in reemplazos:
        texto = texto.replace(a,b)
    
    return texto



def pangrama(texto):

    letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0, 'ñ': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    try:
        for c in texto:
            if (c == '!' or c == '¡' or c == '¿' or c == '?' or c == ' ' or c == ':'):
                continue
            else:
                letras[c] += 1

        print(f"La frase: {texto}")

        print("NO ES UN PANGRAMA") if 0 in letras.values() else print("ES UN PANGRAMA")

    except :
        print("texto con letras distintas al idioma español.")

    
    


def heterograma(texto):
    
    letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0, 'ñ': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    try:
        centinela = True
        for c in texto:
            if (c == '!' or c == '¡' or c == '¿' or c == '?' or c == ' ' or c == ':'):
                continue
            else:
                letras[c] += 1
                if letras[c] > 1:
                    centinela = False
                    break

        print(f"La frase: {texto}")

        print("NO ES UN HETEROGRAMA") if not centinela else print("ES UN HETEROGRAMA")

    except :
        print("texto con letras distintas al idioma español.")

    



def isograma(texto):

    letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
           'n': 0, 'ñ': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    try:
        for c in texto:
            if (c == '!' or c == '¡' or c == '¿' or c == '?' or c == ' ' or c == ':'):
                continue
            else:
                letras[c] += 1  

        print(f"La frase: {texto}")
        
        valores = list(letras.values())

        maximo = max(valores)
        es_isograma = True

        for num in letras:
            if (letras[num] != 0 and letras[num] != maximo):
                es_isograma = False
                break
        
        print("ES UN ISOGRAMA") if es_isograma else print("NO ES UN ISOGRAMA")      

    except :
        print("texto con letras distintas al idioma español.")
        



pangrama(normalizar_cadena("Whisky bueno: ¡excitad mi frágil pequeña vejez!"))

heterograma(normalizar_cadena("centrifugado"))

isograma(normalizar_cadena("deed"))

