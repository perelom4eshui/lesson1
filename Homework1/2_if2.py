"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
#def strings_equal(string_1, string_2):
#    if type(string_1) is str 

input_object_1 = 1
input_object_2 = 'word'

def comparison(object_1, object_2):
    output = ""
    if type(object_1) is str and type(object_2) is str:
        if object_1 == object_2:
            output = 1
        elif len(object_1) > len(object_2):
            output = 2
        elif object_2 == 'learn':
            output = 3
    else:
        output = 0
    return output

input_object_1 = 1
input_object_2 = 'word'
print(comparison(input_object_1, input_object_2))

input_object_1 = 'word'
input_object_2 = 'word'
print(comparison(input_object_1, input_object_2))


input_object_1 = 'words'
input_object_2 = 'word'
print(comparison(input_object_1, input_object_2))


input_object_1 = 'word'
input_object_2 = 'wordss'
print(comparison(input_object_1, input_object_2))

nput_object_1 = 'word'
input_object_2 = 'learn'
print(comparison(input_object_1, input_object_2))

if __name__ == "__main__":
    main()
