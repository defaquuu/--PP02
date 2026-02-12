# car_delivery_tracker.py
from datetime import datetime, timedelta
import random

orders = {
    "A001": {"model": "Lada Granta", "status": "Производство", "days": 10},
    "A002": {"model": "Kia Rio", "status": "Доставка", "days": 5},
    "A003": {"model": "Hyundai Solaris", "status": "Готов к выдаче", "days": 0},
    "A004": {"model": "Toyota Camry", "status": "Производство", "days": 15},
    "A005": {"model": "BMW X5", "status": "Доставка", "days": 7}
}

print("=== ОТСЛЕЖИВАНИЕ ДОСТАВКИ АВТОМОБИЛЯ ===\n")

order_id = input("Введите номер заказа: ").upper()

if order_id in orders:
    car = orders[order_id]
    print(f"\nЗаказ: {order_id}")
    print(f"Модель: {car['model']}")
    print(f"Статус: {car['status']}")
    
    if car['days'] > 0:
        delivery_date = datetime.now() + timedelta(days=car['days'])
        print(f"Осталось дней: {car['days']}")
        print(f"Ориентировочная дата: {delivery_date.strftime('%d.%m.%Y')}")
    else:
        print("Автомобиль готов к выдаче!")
else:
    print("Заказ не найден")