# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GardenWatch
def print_menu():
    print("\n=== GardenWatch: Меню действий ===")
    print("1. Добавить растение")
    print("2. Записать полив/уход")
    print("3. Просмотреть список растений")
    print("4. Удалить растение")
    print("5. Выход")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def main():
    plants = {}  # {id: {"name": str, "watered_at": datetime, "notes": list}}
    
    while True:
        print_menu()
        choice = get_int_input("\nВыберите действие (1-5): ")
        
        if choice == 1:
            name = input("Название растения: ").strip() or "Без названия"
            plants[len(plants) + 1] = {"name": name, "watered_at": None, "notes": []}
            print(f"Растение '{name}' добавлено.")
        elif choice == 2:
            pid = get_int_input("ID растения для ухода (или введите 'all' для всех): ")
            if pid.lower() == 'all':
                for p in plants.values():
                    input_text = f"Полив {p['name']}: "
                    watered_at = datetime.now().strftime("%Y-%m-%d %H:%M")
                    p["watered_at"] = watered_at
            else:
                if pid not in plants: print("ID не найден."); continue
                input_text = f"Полив {plants[pid]['name']}: "
                plants[pid]["watered_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        elif choice == 3:
            if not plants: print("Список пуст.")
            else:
                for pid, p in sorted(plants.items()):
                    status = "Влажно" if p["watered_at"] else "Сухое"
                    print(f"[{pid}] {p['name']} ({status})")
        elif choice == 4:
            pid = get_int_input("ID растения для удаления: ")
            if pid in plants: del plants[pid]; print("Удалено.")
            else: print("Не найдено.")
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
