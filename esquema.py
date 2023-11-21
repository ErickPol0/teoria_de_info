import random
import hashlib

def fuente():
    texto = 'saoko papi saoko'
    return texto

def transmisor(mensaje, tabla_codigos, longitud_paquete):
    mensaje_codificado = "".join(tabla_codigos[caracter] for caracter in mensaje)
    hash_mensaje = calcular_hash(mensaje_codificado)
    mhash = mensaje_codificado+hash_mensaje
    paquetes = [mhash[i:i+longitud_paquete] for i in range(0, len(mhash), longitud_paquete)]
    return paquetes

def adaptacion_modulativa(datos, probabilidad_error):
    paquetes = datos
    paks_completos = [0]*len(paquetes)
    error = True
    intento = 0
    n = len(paks_completos)
    insert_index = list(range(n))
    while error:
        paquetes_recibidos,indx_buenos,paquetes_perdidos,indx_perdido = canal(paquetes, insert_index, probabilidad_error)
        for i in range(len(paquetes_recibidos)):
            paks_completos[indx_buenos[i]] = paquetes_recibidos[i]
        if paks_completos == datos:
            error = False
            return paks_completos
        else:
            intento = intento + 1
            print(f"Intento {intento}: Se perdieron paquetes. Reintentando...")
            insert_index = indx_perdido
            paquetes = paquetes_perdidos
            if intento==20:
                break

def calcular_hash(mensaje_codificado):
    mensaje_codificado = mensaje_codificado.encode('utf-8')
    hash_obj = hashlib.sha256()
    hash_obj.update(mensaje_codificado)
    hash_resultado = hash_obj.hexdigest()
    return hash_resultado

def canal(paquetes,insert_index, probabilidad_error):
    paks_perdidos = []
    paks_recuperados = []
    indx_buenos = []
    indx_malos = []
    for i,pak in enumerate(paquetes):
        p = random.random()
        if p < probabilidad_error:
            paks_perdidos.append(pak)
            indx_malos.append(insert_index[i])
        else:
            paks_recuperados.append(pak)
            indx_buenos.append(insert_index[i])
    return paks_recuperados, indx_buenos, paks_perdidos, indx_malos


def receptor(paquetes_recuperados, tabla_codigos):
    mhash = ''.join(paquetes_recuperados)
    bits = mhash[:-64]
    hashr = mhash[-64:]
    bitshash = calcular_hash(bits)
    if bitshash == hashr:
        texto_decodificado = ""
        codigo_actual = ""
        tabla_inversa = {codigo: simbolo for simbolo, codigo in tabla_codigos.items()}
        for bit in bits:
            codigo_actual += bit
            if codigo_actual in tabla_codigos.values():
                simbolo = tabla_inversa[codigo_actual]
                texto_decodificado += simbolo
                codigo_actual = ""
        return texto_decodificado  
    else:
        print("Error: La integridad del mensaje no es válida. Posible manipulación o pérdida de datos.")  
    
def destino(texto):
    print(texto)

