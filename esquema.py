import random

def fuente():
    texto = 'saoko papi saoko'
    return texto

def transmisor(texto, tabla_codigos, longitud_paquete):
    texto_codificado = "".join(tabla_codigos[caracter] for caracter in texto)
    paquetes = [texto_codificado[i:i+longitud_paquete] for i in range(0, len(texto_codificado), longitud_paquete)]
    return paquetes

def canal(paquetes, probabilidad_error):
    paquetes_perdidos = []
    paquetes_recibidos = []
    
    for paquete in paquetes:
        if random.random() < probabilidad_error:
            paquetes_perdidos.append(paquete)
        else:
            paquetes_recibidos.append(paquete)
    
    return paquetes_recibidos, paquetes_perdidos

def receptor(texto_codificado, tabla_codigos):
    texto_decodificado = ""
    codigo_actual = ""
    tabla_inversa = {codigo: simbolo for simbolo, codigo in tabla_codigos.items()}

    for bit in texto_codificado:
        codigo_actual += bit
        if codigo_actual in tabla_codigos.values():
            simbolo = tabla_inversa[codigo_actual]
            texto_decodificado += simbolo
            codigo_actual = ""

    return texto_decodificado


def destino(texto):
    print(texto)

