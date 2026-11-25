# Линейная консольная программа: расчет стоимости доставки груза
def main():
    weight = float(input("Введите вес груза (кг): "))
    delivery_type = input("Тип доставки (1 - обычная, 2 - экспресс): ")

    if weight <= 0:
        print("Ошибка: вес должен быть положительным числом.")
        return

    if delivery_type == "1":
        cost = weight * 100
    elif delivery_type == "2":
        cost = weight * 200
    else:
        print("Ошибка: выбран неверный тип доставки.")
        return

    if weight > 10:
        cost += 500

    print(f"Итоговая стоимость доставки: {cost:.2f} руб.")

main()
