# Конвертер времени в миллисекунды

# Запрашиваем у пользователя часы, минуты, секунды
hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))
seconds = int(input("Введите секунды: "))

# Формула преобразования:
# часы → секунды: часы * 3600
# минуты → секунды: минуты * 60
# секунды → миллисекунды: * 1000

total_seconds = hours * 3600 + minutes * 60 + seconds
milliseconds = total_seconds * 1000

# Выводим результат
print(f"\n⏱ Результат:")
print(f"{hours}ч {minutes}м {seconds}с = {milliseconds} миллисекунд")
print(f"Или: {total_seconds} секунд")
