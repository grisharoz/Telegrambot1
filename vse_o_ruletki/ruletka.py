# -*- coding: utf-8 -*-
import random
from listruletki_object import list_of_roulette


print("Приветствую! Рады видеть тебя в одной из увлекательной и фартовой игре в мире:")
print("\nСупер! Давай поскорее начнём играть)")

choice = ""

while True:
    try:
        # TODO 1: add balance calculation
        money = int(input("Cколько ты хочешь поставить?:"))
    except ValueError:
        print("Такой ставки нет в списке. Попробуй ещё раз")
        continue

    bet = input(
        "Выбери из переченя:'число','цвет','старшинство','ряд,'совокупность чисел','столбец','последовательность 'чётность':"
    )

    options = [
        "число",
        "цвет",
        "старшинство",
        "ряд",
        "совокупность чисел",
        "столбец",
        "последовательность",
        "чётность",
    ]

    if bet not in options:
        print("Такой ставки нет в списке. Попробуй ещё раз")
        continue

    my_list = [money]

    if bet == "число":
        choice = input("Какое именно число от 0 дро 36 ты хочешь выбрать?:")
        my_list.append(choice)

        if choice not in [str(i) for i in range(0, 37)]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "цвет":
        choice = input("Какой именно цвет ты хочешь выбрать?(красное, чёрное):")
        my_list.append(choice)

        if choice not in ["красное", "чёрное"]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "старшинство":
        choice = input(
            "Какую именно последовательность ты хочешь выбрать?(1/18 or 19/36):"
        )
        my_list.append(choice)

        if choice not in ["1/18", "19/36"]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "ряд":
        choice = input("Какой именно ряд ты хочешь выбрать(1,2,3)?:")
        my_list.append(choice)

        if choice not in ["1", "2", "3"]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "совокупность чисел":
        choice = input(
            "Какую именно совокупность чисел ты хочешь выбрать?(напиши её через слэш):"
        )
        my_list.append(choice)

    if bet == "столбец":
        choice = input("Какой именно столбец ты хочешь выбрать?(1-12):")
        my_list.append(choice)
        if choice not in [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        ]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "последовательность":
        choice = input(
            "Какую именно последовательность ты хочешь выбрать?(1-12/13-24/25-36):"
        )
        my_list.append(choice)
        if choice not in ["1-12", "13-24", "25-36"]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    if bet == "чётность":
        choice = input("Ты выберишь чётное или нечётное?:")
        my_list.append(choice)
        if choice not in ["чётное", "нечётное"]:
            print("Введена неправильная информация. Попробуй ещё раз.")
            continue

    again = input("Хочешь сделать ещё ставку?(да/нет):")
    if again == "да":
        continue
    elif again == "нет":
        print(
            "Рулетка крутиться!\nКто знает, может тебе сегодня улыбнётся удача??\nНа рулетке выпало:"
        )
        rand = random.choice(list(list_of_roulette))
        print(rand)

        if bet == "совокупность чисел":
            if choice in list_of_roulette[rand][bet]:
                money *= 3
                print("Ты выиграл! Вот твой выигрыш:", money)
            else:
                print("Ты проиграл, но не расстраивайся :)")
        else: 
            if list_of_roulette[rand][bet]["значение"] == choice:
                money *= list_of_roulette[rand][bet]["коеффициент"]
                print("Ты выиграл! Вот твой выигрыш:", money)
            else:
                print("Ты проиграл, но не расстраивайся :)")

    else:
        print("Такого нет вариант")
        continue

    ending = input("\nТы хочешь ещё раз сыграть?:")
    if ending == "да":
        continue
    if ending == "нет":
        break
