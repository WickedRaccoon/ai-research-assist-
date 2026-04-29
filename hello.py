# Программа управления задачами (TODO List)

tasks = []  # Список для хранения задач

def add_task(task_name):
    """Функция для добавления новой задачи в список"""
    tasks.append(task_name)
    print(f"✓ Задача '{task_name}' добавлена!")

def show_tasks():
    """Функция для отображения всех задач"""
    if not tasks:
        print("Список задач пуст")
        return
    
    print("\n📋 Ваши задачи:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    print()

def delete_task():
    """Функция для удаления задачи по номеру"""
    if not tasks:
        print("Список задач пуст")
        return
    
    show_tasks()
    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"✓ Задача '{removed_task}' удалена!")
        else:
            print(f"❌ Неверный номер. Выберите от 1 до {len(tasks)}")
    except ValueError:
        print("❌ Введите корректный номер")

# Основное меню программы
while True:
    print("\n--- ГЛАВНОЕ МЕНЮ ---")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу")
    print("4. Выход")
    
    choice = input("Выберите действие (1-4): ")
    
    if choice == "1":
        new_task = input("Введите название задачи: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("До свидания!")
        break
    else:
        print("❌ Неверный выбор. Попробуйте снова.")
