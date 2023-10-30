class LZWCompressor:
    def __init__(self):
        self.dictionary = {chr(i): i for i in range(256)}
        self.current_code = 256

    def create_symbol_table(self, data):
        symbol_table = {chr(i): i for i in range(256)}
        current_code = 256
        prefix = ""

        for symbol in data:
            extended_prefix = prefix + symbol
            if extended_prefix not in symbol_table:
                symbol_table[extended_prefix] = current_code
                current_code += 1
            prefix = symbol

        return symbol_table


# Ejemplo de uso
lzw = LZWCompressor()
original_data = "ABABABA"
symbol_table = lzw.create_symbol_table(original_data)

print("Tabla de Símbolos:", symbol_table)
