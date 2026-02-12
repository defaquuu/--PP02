# car_service_history.py
from datetime import datetime

service_history = {}

print("=== ИСТОРИЯ ОБСЛУЖИВАНИЯ АВТОМОБИЛЯ ===\n")

while True:
    print("\n1. Добавить запись об обслуживании")
    print("2. Показать историю")
    print("3. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        vin = input("VIN автомобиля: ").upper()
        date = datetime.now().strftime("%d.%m.%Y")
        service_type = input("Тип обслуживания: ")
        mileage = input("Пробег (км): ")
        cost = input("Стоимость (руб): ")
        notes = input("Примечания: ")
        
        record = {
            "date": date,
            "service_type": service_type,
            "mileage": mileage,
            "cost": cost,
            "notes": notes
        }
        
        if vin not in service_history:
            service_history[vin] = []
        
        service_history[vin].append(record)
        print("Запись добавлена!")
    
    elif choice == "2":
        vin = input("VIN автомобиля: ").upper()
        
        if vin in service_history and service_history[vin]:
            print(f"\nИстория обслуживания VIN: {vin}")
            print("-" * 50)
            total_cost = 0
            for i, record in enumerate(service_history[vin], 1):
                print(f"{i}. Дата: {record['date']}")
                print(f"   Тип: {record['service_type']}")
                print(f"   Пробег: {record['mileage']} км")
                print(f"   Стоимость: {record['cost']} руб.")
                if record['notes']:
                    print(f"   Прим.: {record['notes']}")
                print()
                total_cost += int(record['cost']) if record['cost'].isdigit() else 0
            print(f"Общая стоимость обслуживания: {total_cost} руб.")
        else:
            print("История обслуживания не найдена")
    
    elif choice == "3":
        print("Выход")
        break