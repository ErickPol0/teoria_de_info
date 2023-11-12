from esquema import *
from huffman import CodificacionHuffman
from shannon_fano import ShannonFano

metodo = int(input('Decida el metodo de codificacion:\n1 - Hoffman\n2 - Shannon\n'))
if metodo == 1:
    codificador = CodificacionHuffman()

else:
    codificador = ShannonFano()


longitud_paquete = 4  # Puedes ajustar este valor según tus necesidades
probabilidad_error = 0.3  # Puedes ajustar la probabilidad de error
texto_original = fuente()
tabla_codigos = codificador.tabla(texto_original)
paquetes = transmisor(texto_original, tabla_codigos, longitud_paquete)
paquetes_recibidos, paquetes_perdidos = canal(paquetes, probabilidad_error)


#texto_codificado= canal(texto_codificado)
#texto_decodificado = receptor(texto_codificado,tabla_codigos)
#destino(texto_decodificado)
#holaaa


    







