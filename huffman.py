import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

class CodificacionHuffman:
    def __init__(self):
        pass

    def construir_arbol_huffman(self, frecuencias):
        cola_prioridad = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in frecuencias.items()]
        heapq.heapify(cola_prioridad)

        while len(cola_prioridad) > 1:
            nodo1 = heapq.heappop(cola_prioridad)
            nodo2 = heapq.heappop(cola_prioridad)
            nuevo_nodo = NodoHuffman(None, nodo1.frecuencia + nodo2.frecuencia)
            nuevo_nodo.izquierda = nodo1
            nuevo_nodo.derecha = nodo2
            heapq.heappush(cola_prioridad, nuevo_nodo)

        return cola_prioridad[0]

    def generar_codigos_huffman(self, arbol, prefijo="", codigos=None):
        if codigos is None:
            codigos = {}
        if arbol.simbolo is not None:
            codigos[arbol.simbolo] = prefijo
        if arbol.izquierda is not None:
            self.generar_codigos_huffman(arbol.izquierda, prefijo + "0", codigos)
        if arbol.derecha is not None:
            self.generar_codigos_huffman(arbol.derecha, prefijo + "1", codigos)
        return codigos
    
    def generar_tabla_codigos_huffman(self, codigos):
        tabla_codigos = {}
        for simbolo, codigo in codigos.items():
            tabla_codigos[simbolo] = codigo
        return tabla_codigos

    def tabla(self, texto):
        frecuencias = defaultdict(int)
        for caracter in texto:
            frecuencias[caracter] += 1

        arbol = self.construir_arbol_huffman(frecuencias)
        codigos = self.generar_codigos_huffman(arbol)
        tabla_codigos = self.generar_tabla_codigos_huffman(codigos)
        return tabla_codigos