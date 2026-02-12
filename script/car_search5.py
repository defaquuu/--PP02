# car_search.py
cars = [
    {"model": "Lada Granta", "price": 700000},
    {"model": "Lada Vesta", "price": 950000},
    {"model": "Kia Rio", "price": 1200000},
    {"model": "Hyundai Solaris", "price": 1300000},
    {"model": "Skoda Octavia", "price": 1800000},
    {"model": "Toyota Camry", "price": 2500000},
    {"model": "BMW X5", "price": 5500000},
    {"model": "Audi Q7", "price": 6200000}
]

print("=== ПОИСК АВТОМОБИЛЕЙ ПО ЦЕНЕ ===\n")

try:
    max_price = int(input("Введите максимальную цену (руб): "))
    print(f"\nАвтомобили до {max_price:,} руб.:\n".replace(",", " "))
    
    found = False
    for car in cars:
        if car["price"] <= max_price:
            print(f"   • {car['model']}: {car['price']:,} руб.".replace(",", " "))
            found = True
    
    if not found:
        print("   Нет автомобилей в этом бюджете")
except ValueError:
    print("Ошибка: введите число")