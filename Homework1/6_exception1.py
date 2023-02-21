"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def hello_user3():
    try:
      while input('Как дела? ') != 'Хорошо':
        print('') 
    except KeyboardInterrupt:
      print('\nПока!')

def hello_user2():
  try:
    while True:
      if input('Как дела? ') == 'Хорошо': 
        print('Пока!')
        break
      
  except KeyboardInterrupt:
    print('\n Пока!')

def hello_user():
    while True:
      try:
        if input('Как дела? ') == 'Хорошо': 
          print('Пока!')
          break
      except KeyboardInterrupt:
        print('Пока!')
        break
  
   
      

if __name__ == "__main__":
    hello_user()
