def raining():
    user_input = input("Какая сегодня погода? " )
    if user_input.lower() == "Солнечная":
        print("Возьми с собой очки")
    else:
        print("Возьми с собой зонт")
    print("Хорошего дня!")


raining()
