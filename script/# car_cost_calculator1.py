# car_cost_calculator.py
print("=== КАЛЬКУЛЯТОР СТОИМОСТИ АВТОМОБИЛЯ ===\n")

base_price = 1000000

print("Выберите двигатель:")
print("1 - Бензин 1.6 (0 руб.)")
print("2 - Дизель 2.0 (+200 000 руб.)")
print("3 - Электро (+500 000 руб.)")
engine = int(input("Ваш выбор (1-3): "))

print("\nВыберите коробку:")
print("1 - Механика (0 руб.)")
print("2 - Автомат (+150 000 руб.)")
gearbox = int(input("Ваш выбор (1-2): "))

print("\nДоп. опции:")
color = input("Металлик? (+30 000) (да/нет): ").lower()
climate = input("Климат-контроль? (+50 000) (да/нет): ").lower()

price = base_price

if engine == 2:
    price += 200000
elif engine == 3:
    price += 500000

if gearbox == 2:
    price += 150000
if color == "да":
    price += 30000
if climate == "да":
    price += 50000

print(f"\nИТОГОВАЯ СТОИМОСТЬ: {price} руб.")