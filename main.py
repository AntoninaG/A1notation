def getLetter(num):
    # Согласно таблице ASCII - код 65 = A
    offset = 65 
    # Функция chr преобразует число в символ
    remainder = num % 26
    return chr(offset + remainder)

# Принимает номер столбца в качестве аргумента и
# возвращает имя столбца как в Экселе.
def convert(num):
    if num < 26:
        return getLetter(num)
    return convert(num // 26) + getLetter(num)

    
def convert_old(num):
    if num < 26:
        return getLetter(num)
    if num < 676:
        result = num // 26
        return getLetter(result) + getLetter(num)
    result1 = num // 26
    result2 = result1 // 26
    return getLetter(result2) + getLetter(result1)+ getLetter(num)

def printAscii():
    for n in range(0, 256):
        print("%d = %s" % (n, chr(n)))
    #    print (str(n) + " = " + chr(n))