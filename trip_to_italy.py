def convert(dollars):
    rub = dollars * 70.38
    euro = rub/(100/1.22)

    return euro


while True:
    user_input = int(input('Введите количество $: '))
    if user_input == 'стоп':
        break
    count = convert(user_input)
    print(count)
