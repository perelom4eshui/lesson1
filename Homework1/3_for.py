"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phone_sell = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    
    
    def phone_summary(phone_sells):
        phone_sell_summ = 0
        for daily_sell in phone_sells:
            phone_sell_summ += daily_sell
        return phone_sell_summ
      
    summ_sell = 0
    summ_len = 0

    for phone in phone_sell:
        print(f"Общее количество проданных {phone['product']}: {phone_summary(phone['items_sold'])}шт.")
        print(f"Среднее количество проданных {phone['product']}: {phone_summary(phone['items_sold'])/len(phone['items_sold'])}шт.")
        print('')
        summ_sell += phone_summary(phone['items_sold'])
        summ_len += len(phone['items_sold'])

    
    print ('')
    print (f'Общее количесвто проданных телефонов: {summ_sell}')
    print (f'Среднее количесвто проданных телефонов: {summ_sell/summ_len}')    
if __name__ == "__main__":
    main()
