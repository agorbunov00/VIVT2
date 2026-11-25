# Модульная консольная программа: расчет стоимости доставки груза

def validate_weight(weight):
    return weight > 0

def calc_base_cost(weight, delivery_type):
    if delivery_type == "1":
        return weight * 100
    elif delivery_type == "2":
        return weight * 200
    return None

def apply_heavy_fee(cost, weight):
    if weight > 10:
        return cost + 500
    return cost

def main():
    weight = float(input("Введите вес груза (кг): "))
    delivery_type = input("Тип доставки (1 - обычная, 2 - экспресс): ")

    if not validate_weight(weight):
        print("Ошибка: вес должен быть положительным числом.")
        return

    cost = calc_base_cost(weight, delivery_type)
    if cost is None:
        print("Ошибка: выбран неверный тип доставки.")
        return

    total_cost = apply_heavy_fee(cost, weight)
    print(f"Итоговая стоимость доставки: {total_cost:.2f} руб.")

if __name__ == "__main__":
    main()
