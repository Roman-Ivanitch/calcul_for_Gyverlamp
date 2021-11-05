import math
import os

def calculations():
    delivery = 400 # примерная привычная стоимость доставки постой России
    PI = math.pi
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print("Расчет длинны и стоимости ленты для GyverLamp")
    print("______________________________________________________")
    print("Данные вводите в милиметрах мм")

    diameter = int(input("Ведите диаметр основания лампы : "))
    h = int(input("Ведите высоту основания лампы : "))
    width = int(input("Ведите ширину ленты: "))
    otvet = input("Будетли шаг между лентой? да или нет: ")
    if otvet == "да": 
        width_step = int(input("Ведите ширину шага: ")) 
        width += width_step
    else:
        print("что-то не коректное ввели, по умолчанию лента наматываеться в плотную")

    cost = int(input("Сколько стоит 1 метр ленты(в рублях): "))

    print()

    length = round(diameter * PI)       # округлённая длина окружности 
    general_h = h / width               # высота делённая на ширину ленты = сколько лекты в ряд
    metr_led = length * general_h       # длина ленты нам надо в мм
    metr_led = round(metr_led) / 1000   # округлённая длина ленты нам надо в метрах 
    by = cost * math.ceil(metr_led)     # сколько вся лента будет стоить 
                                        # я техник, а не русовед!
    print(f"Нужно {metr_led} метров адресной ленты") 
    print(f"Лента обойдёться в {by} рублей + {delivery} доставка") 
    print(f"Итого: {by + delivery} рублей")
    print("Это много! ") if (by > 5000 ) else 0
    print("______________________________________________________")
    input()

def main():
    while True:
        calculations()

if __name__ == "__main__":
    main()