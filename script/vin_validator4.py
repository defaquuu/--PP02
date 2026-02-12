# vin_validator.py
def check_vin(vin):
    vin = vin.upper()
    if len(vin) != 17:
        return False, f"Неверная длина: {len(vin)} символов (нужно 17)"
    
    allowed_chars = "ABCDEFGHJKLMNPRSTUVWXYZ0123456789"
    for char in vin:
        if char not in allowed_chars:
            return False, f"Недопустимый символ: {char}"
    
    return True, "VIN-номер корректен"

print("=== ПРОВЕРКА VIN-НОМЕРА ===\n")
vin = input("Введите VIN (17 символов): ")
is_valid, message = check_vin(vin)
print(message)