# license_plate_generator.py
import random

def generate_plate():
    letters = "АВЕКМНОРСТУХ"
    numbers = "0123456789"
    
    letter1 = random.choice(letters)
    digits = "".join(random.choice(numbers) for _ in range(3))
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    region = random.choice(["777", "77", "50", "90", "116", "178", "197", "799"])
    
    return f"{letter1}{digits}{letter2}{letter3} {region}"

print("=== ГЕНЕРАТОР ГОСНОМЕРОВ РФ ===\n")

try:
    count = int(input("Сколько номеров сгенерировать? "))
    print("\nСгенерированные номера:\n")
    for i in range(count):
        print(f"{i+1:2}. {generate_plate()}")
except ValueError:
    print("Ошибка: введите число")