def check_weather(temperature):
    if temperature < 0:
        return('На улице холодно')
    elif temperature >= 0 and temperature < 15:
        return('На улице прохладно')
    elif temperature >= 15 and temperature < 25:
        return('На улице тепло')
    else:
        return 'На улице жарко!'
    return 'Не работает!'

print(check_weather(-10))   # На улице холодно
print(check_weather(8))     # На  улице прохладно
print(check_weather(20))    # На  улице тепло
print(check_weather(40))    # На  улице жарко