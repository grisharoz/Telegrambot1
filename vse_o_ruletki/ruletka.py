# -*- coding: utf-8 -*-
import random
from listruletki_object import list_of_roulette

while True:
    start=input("Приветствую! Рады видеть тебя в одной из увлекательной и фартовой игре в мире :)\nГотов ли ты попытать свою удачу?(Выбери да/нет):")

    if start not in ["да", "нет"]:
        print("Такого варианта нет")
        continue

    break


if start=="да":
    print("\nСупер! Давай поскорее начнём играть)")
    choice=""
    str_type:str=''

    while True:
        try:
            money=int(input('Cколько ты хочешь поставить?:'))
        except ValueError:
            print("Такой ставки нет в списке. Попробуй ещё раз")
            continue

        bet=input("Выбери из переченя:'число','красное/чёрное','старшинство','ряд,'совокупность чисел','столбец','последовательность ',чётное/нечётное':")


        options = ["число", "красное/чёрное", "старшинство", "ряд", "совокупность чисел", "столбец", "последовательность", "чётное/нечётное"]

        if bet not in options:
            print("Такой ставки нет в списке. Попробуй ещё раз")
            continue


        my_list=[money]



        if bet=='число':
            choice=input("Какое именно число от 0 дро 36 ты хочешь выбрать?:")
            my_list.append(choice)

            if choice not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue


        if bet=='красное/чёрное':
            choice=input("Какой именно цвет ты хочешь выбрать?:")
            my_list.append(choice)

            if choice not in ['красное','чёрное']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue


        if bet=='старшинство':
            choice = input("Какую именно последовательность ты хочешь выбрать?(1-18/19-36):")
            my_list.append(choice)

            if choice not in ['1-18','19-36']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue


        if bet=="ряд":
            choice = input("Какой именно ряд ты хочешь выбрать(1,2,3)?:")
            my_list.append(choice)

            if choice not in ['1','2','3']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue



        if bet=='cовокупность':
            choice = input("Какую именно совокупность чисел ты хочешь выбрать?(напиши её через слэш):")
            my_list.append(choice)




        if bet=='столбец':
            choice = input("Какой именно столбец ты хочешь выбрать?(1-12):")
            my_list.append(choice)
            if choice not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue


        if bet=='последователность':
            choice = input("Какую именно последовательность ты хочешь выбрать?(1-12/13-24/25-36):")
            my_list.append(choice)
            if choice not in ['1-12','13-24','25-36']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue



        if bet=='чётное/нечётное':
            choice = input("Ты выберишь чётное или нечётное?:")
            my_list.append(choice)
            if choice not in ['чётное','нечётное']:
                print("Введена неправильная информация. Попробуй ещё раз.")
                continue



        again = input('Хочешь сделать ещё ставку?(да/нет):')
        if again == 'да':
            continue
        elif again == 'нет':
            print("Рулетка крутиться!\nКто знает, может тебе сегодня улыбнётся удача??\nНа рулетке выпало:")
            rand=random.choice(list(list_of_roulette))
            print(rand)




            if list_of_roulette[choice][bet]==choice:
                money +=1
                print("Ты выиграл! Вот твой выигрыш:",money)
            else:
                print("Ты проиграл, но не расстраивайся :)")


                break
        else:
            print("Такого нет вариант")
            continue

        ending=input('\nТы хочешь ещё раз сыграть?:')
        if ending=="да":
            continue
        if ending=='нет':
            break

if start=="нет":
    print("\nПечально :(\nНо ты заходи если что. До следующего раза :)")
