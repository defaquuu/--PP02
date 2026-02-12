# auto_parts_store.py
warehouse = {
    "фильтр масляный": 45,
    "тормозные колодки": 120,
    "свеча зажигания": 200,
    "ремень ГРМ": 30,
    "масло моторное": 80,
    "воздушный фильтр": 55,
    "стартер": 12,
    "генератор": 8
}

print("=== СКЛАД АВТОЗАПЧАСТЕЙ ===\n")
print("Остатки на складе:\n")

for part, quantity in warehouse.items():
    print(f"{part.capitalize()}: {quantity} шт.")

print("\n" + "-" * 30)
search = input("Проверить наличие детали: ").lower()

if search in warehouse:
    print(f"{search.capitalize()} в наличии: {warehouse[search]} шт.")
else:
    print(f"Деталь '{search}' не найдена")