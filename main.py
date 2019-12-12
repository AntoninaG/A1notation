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
