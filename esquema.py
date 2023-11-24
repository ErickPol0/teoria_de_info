import random
import hashlib

def fuente():
    texto = 'saoko papi saoko'
    return texto

def transmisor(mensaje, tabla_codigos, longitud_paquete):
    print('tabla original ',tabla_codigos)
    hashtabla = hash_table(tabla_codigos)
    hash_mensaje = hash_message(mensaje,hashtabla)
    print('mensaje hash:',hash_mensaje)
    print('tabla hash:',hashtabla)
    paquetes = [hash_mensaje[i:i+longitud_paquete] for i in range(0, len(hash_mensaje), longitud_paquete)]
    return paquetes,hashtabla

def modulacion_adaptativa(datos, probabilidad_error):
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

def hash_table(symbol_table):
    hashed_table = {}
    for symbol, bits in symbol_table.items():
        hashed_value = hashlib.sha256(bits.encode()).hexdigest()
        hashed_table[symbol] = hashed_value
    return hashed_table

def hash_message(message, hashed_table):
    hashed_message = ''
    for s in message:
        hashed_value = hashed_table.get(s, "DESCONOCIDO")
        hashed_message += hashed_value
    return hashed_message

def receptor(hashed_table, hashed_paquetes):
    hashed_table = list(hashed_table.items())
    hashed_table = sorted(hashed_table, key=lambda x: x[1])  # Ordenar por hash
    hashed_message = ''.join(hashed_paquetes)
    decoded_message = ""
    # Dividir el mensaje hasheado en secuencias de bits
    secuencias_hash = [hashed_message[i:i+64] for i in range(0, len(hashed_message), 64)]
    for secuencia in secuencias_hash:
        # Utilizar la búsqueda binaria para obtener el símbolo correspondiente
        symbol = binary_search(hashed_table, secuencia)
        if symbol is not None:
            decoded_message += symbol
        else:
            decoded_message += "DESCONOCIDO"  # Marcar si el símbolo no fue encontrado
    return decoded_message

def binary_search(hashed_table, secuencia):
    left, right = 0, len(hashed_table) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_key, mid_value = hashed_table[mid]
        if mid_value == secuencia:
            return mid_key  # Se encontró la secuencia de bits, devuelve el símbolo
        elif mid_value < secuencia:
            left = mid + 1
        else:
            right = mid - 1
    return None

def destino(texto):
    print(texto)

