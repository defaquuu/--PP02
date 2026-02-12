# fuel_consumption.py
print("=== РАСЧЁТ РАСХОДА ТОПЛИВА ===\n")

distance = float(input("Пройденное расстояние (км): "))
fuel = float(input("Израсходовано топлива (л): "))

consumption = (fuel / distance) * 100

print(f"\nСредний расход: {consumption:.1f} л/100 км")

if consumption < 6:
    rating = "Отлично"
elif consumption < 8:
    rating = "Хорошо"
elif consumption < 10:
    rating = "Средне"
elif consumption < 12:
    rating = "Высокий"
else:
    rating = "Очень высокий"

print(f"Оценка: {rating}")

price_per_liter = float(input("\nЦена за литр (руб): "))
cost = fuel * price_per_liter
print(f"Стоимость поездки: {cost:.2f} руб.")
print(f"Стоимость 1 км: {cost/distance:.2f} руб.")