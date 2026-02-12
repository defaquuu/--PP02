# service_queue.py
from collections import deque
import time

service_queue = deque()

print("=== СИСТЕМА ЗАПИСИ НА ТО ===\n")

while True:
    print("\n1. Добавить клиента")
    print("2. Обслужить клиента")
    print("3. Показать очередь")
    print("4. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        name = input("Имя клиента: ")
        car = input("Марка автомобиля: ")
        service_queue.append((name, car))
        print(f"{name} ({car}) добавлен в очередь")
    
    elif choice == "2":
        if service_queue:
            client, car = service_queue.popleft()
            print(f"Обслуживается: {client}, автомобиль {car}")
            time.sleep(1)
            print(f"{client} обслужен")
        else:
            print("Очередь пуста")
    
    elif choice == "3":
        print("\nТекущая очередь:")
        if service_queue:
            for i, (client, car) in enumerate(service_queue, 1):
                print(f"   {i}. {client} - {car}")
        else:
            print("   Очереди нет")
    
    elif choice == "4":
        print("Выход")
        break