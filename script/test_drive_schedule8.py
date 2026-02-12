# test_drive_schedule.py
from datetime import datetime, timedelta

schedule = {}

print("=== ЗАПИСЬ НА ТЕСТ-ДРАЙВ ===\n")

while True:
    print("\n1. Записаться")
    print("2. Отменить запись")
    print("3. Показать записи")
    print("4. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        name = input("Ваше имя: ")
        phone = input("Телефон: ")
        model = input("Модель для тест-драйва: ")
        date = input("Дата (ДД.ММ.ГГГГ): ")
        time = input("Время (ЧЧ:ММ): ")
        
        key = f"{date} {time}"
        if key in schedule:
            print("Это время уже занято!")
        else:
            schedule[key] = {
                "name": name,
                "phone": phone,
                "model": model
            }
            print("Запись подтверждена!")
    
    elif choice == "2":
        date = input("Введите дату записи (ДД.ММ.ГГГГ): ")
        time = input("Введите время (ЧЧ:ММ): ")
        key = f"{date} {time}"
        
        if key in schedule:
            del schedule[key]
            print("Запись отменена")
        else:
            print("Запись не найдена")
    
    elif choice == "3":
        print("\nТекущие записи:")
        if schedule:
            for key, value in sorted(schedule.items()):
                print(f"{key} - {value['name']}, {value['model']}")
        else:
            print("Нет записей")
    
    elif choice == "4":
        print("Выход")
        break