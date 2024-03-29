def getLetter(num):
    # Согласно таблице ASCII - код 65 = A
    offset = 65 
    remainder = num % 26
    if remainder == 0:
        return 'Z'
    # Функция chr преобразует число в символ
    return chr(offset + remainder - 1)

# Принимает номер столбца в качестве аргумента и
# возвращает имя столбца как в Экселе.
def convert(num):
    if num < 27:
        return getLetter(num)
    elif num % 26 == 0:
        return convert(num // 26 - 1) + getLetter(num)
    return convert(num // 26) + getLetter(num)
