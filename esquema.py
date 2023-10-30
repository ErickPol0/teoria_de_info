def fuente():
    texto = 'saoko papi saoko'
    return texto

def transmisor(texto, tabla_codigos):
    texto_codificado = "".join(tabla_codigos[caracter] for caracter in texto)
    return texto_codificado

def canal(texto_codificado):
    return texto_codificado

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

