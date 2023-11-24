from esquema import *
from huffman import CodificacionHuffman
from shannon_fano import ShannonFano

metodo = int(input('Decida el metodo de codificacion:\n1 - Hoffman\n2 - Shannon\n'))
if metodo == 1:
    codificador = CodificacionHuffman()
else:
    codificador = ShannonFano()

longitud_paquete = 12
probabilidad_error = 0.4
texto_original = fuente()
tabla_codigos = codificador.tabla(texto_original)
paquetes,tabla_hash = transmisor(texto_original, tabla_codigos, longitud_paquete)
paquetes_recuperados = modulacion_adaptativa(paquetes, probabilidad_error)
texto_decodificado = receptor(tabla_hash,paquetes_recuperados)
destino(texto_decodificado)


    







