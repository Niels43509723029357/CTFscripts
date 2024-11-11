input_file = input('Tekst bestand: ')
output_file = input('output file: ')
with open(input_file, 'r') as file:
    lines = file.readlines()
    binary_string = ''
    for line in lines:
        for word in line.split():
            if word == 'YODA':
                binary_string += '0'
            elif word == 'BABY':
                binary_string += '1'
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))
    with open(output_file, 'wb') as file:
        file.write(byte_array)
