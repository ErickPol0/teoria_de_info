from collections import Counter

class ShannonFano:
    def __init__(self):
        self.codigos = {}

    def calcular_probabilidades(self, texto):
        frecuencias = Counter(texto)
        total_caracteres = len(texto)
        probabilidades = {caracter: frecuencia / total_caracteres for caracter, frecuencia in frecuencias.items()}
        return probabilidades

    def tabla(self, texto):
        probabilidades = self.calcular_probabilidades(texto)
        simbolos = sorted(probabilidades, key=lambda simbolo: probabilidades[simbolo], reverse=True)
        self.generar_codigos(simbolos, probabilidades)
        return self.codigos

    def generar_codigos(self, simbolos, probabilidades):
        n = len(simbolos)
        stack = [(simbolos, probabilidades, "", 0, n - 1)]
        iteraciones = 0  # Contador de iteraciones

        while stack:
            simbolos, probabilidades, prefijo, inicio, fin = stack.pop()
            if inicio == fin:
                self.codigos[simbolos[inicio]] = prefijo
            elif inicio < fin:
                split = self.encontrar_split_index(simbolos, probabilidades, inicio, fin)
                stack.append((simbolos, probabilidades, prefijo + "0", inicio, split))
                stack.append((simbolos, probabilidades, prefijo + "1", split + 1, fin))
            
            iteraciones += 1
            if iteraciones >= 100:  # Límite de iteraciones
                print("Se alcanzó el límite de 100 iteraciones. La generación de códigos se detiene.")
                break

    def encontrar_split_index(self, simbolos, probabilidades, inicio, fin):
        total_probabilidad = sum(probabilidades[simbolo] for simbolo in simbolos[inicio:fin + 1])
        acumulado = 0.0
        split_index = inicio - 1
        for i in range(inicio, fin + 1):
            acumulado += probabilidades[simbolos[i]]
            if acumulado >= total_probabilidad / 2:
                split_index = i
                break
        return split_index
    
