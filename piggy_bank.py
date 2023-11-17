def piggy_bank():
    count_month = 0
    count_money = 0

    while count_month < 12:
        user_input = int(input('Какую сумму внести? \n'))
        count_money += user_input
        count_month +=1
        print('Ждем один месяц')

    return count_money


print(piggy_bank())