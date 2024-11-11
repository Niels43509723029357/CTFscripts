with open(input('filepath: '), 'r') as file:
    lines = file.readlines()
    counts = [line.count("BAND") for line in lines]
    print(counts)
    result =''.join([chr(count+96) for count in counts if count>0])
    print(result)
