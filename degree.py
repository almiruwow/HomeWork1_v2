def degree_conversion(fahrenheit):
    сelsius = (fahrenheit-32) * 5/9
    return сelsius


while True:
    user_input = int(input('Введите градусы: '))
    if user_input == 'стоп':
        break
    cels = degree_conversion(user_input)
    print(cels)
