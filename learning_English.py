def english():
    count = 0

    user_input = input("Привет! Предлагаю проверить свои знания английского! Набери 'ready', чтобы начать! ")
    if user_input.lower() == "ready":
        print("1 Задание")
        print("My name ___ Vova")

        user_input = input('Введите правильный ответ:\n')

        if user_input == "is":
            print("Ответ верный!")
            count += 1
        else:
            print("Неправильно. Правильный ответ: is")

        print("2 Задание")
        print("I ___ a coder")

        user_input = input('Введите правильный ответ:\n')

        if user_input == "am":
            print("Ответ верный!")
            count += 1
        else:
            print("Неправильно. Правильный ответ: am")

        print("3 Задание")
        print("I live ___ Moscow")

        user_input = input('Введите правильный ответ:\n')

        if user_input == "in":
            print("Ответ верный!")
            count += 1
        else:
            print("Неправильно. Правильный ответ: in")

        print(f'Вот и всё! Вы ответили на {count} вопросов из 3 верно, это {(count*100)/3} процентов.')

english()
