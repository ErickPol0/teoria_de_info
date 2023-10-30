from esquema import *
from huffman import CodificacionHuffman
from shannon_fano import ShannonFano

texto_original = fuente()

metodo = int(input('Decida el metodo de codificacion:\n1 - Hoffman\n2 - Shannon\n'))
if metodo == 1:
    codificador = CodificacionHuffman()
    tabla_codigos = codificador.tabla(texto_original)
    texto_codificado = transmisor(texto_original,tabla_codigos)
    texto_codificado= canal(texto_codificado)
    texto_decodificado = receptor(texto_codificado,tabla_codigos)
    destino(texto_decodificado)

else:
    codificador = ShannonFano()
    tabla_codigos = codificador.tabla(texto_original)
    texto_codificado = transmisor(texto_original,tabla_codigos)
    texto_codificado = canal(texto_codificado)
    texto_decodificado = receptor(texto_codificado,tabla_codigos)
    destino(texto_decodificado)


    







