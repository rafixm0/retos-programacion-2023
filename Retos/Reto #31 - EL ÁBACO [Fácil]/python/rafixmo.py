# Reto de programación de MoureDev #31

entrada = ["O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"]

# Resultado: 1.302.790

def obtenerNumeroAbacco(numero):
    total = 0;
    for car in numero:
        if car == '-':
            return total
        else:
            total += 1
    return total
    

def contarAbaco (abacco):
    
    i = 1
    resultado = []

    for numero in abacco:
        resultado.append(obtenerNumeroAbacco(numero))
        if (i == 1 or i == 5): 
            resultado.append('.')
            i += 1
        i+=1

    print(''.join(str(e) for e in resultado))


contarAbaco(entrada)