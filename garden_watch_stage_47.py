# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GardenWatch
def demo():
    """Показывает основной пользовательский сценарий GardenWatch."""
    print("=== Demo GardenWatch ===")
    print()

    # Создаём несколько растений
    plants = [
        Plant("Tomato", "Red", 30),
        Plant("Basil", "Green", 15),
        Plant("Mint", "Green", 20),
    ]

    # Добавляем растения в коллекцию
    collection = PlantCollection()
    for plant in plants:
        collection.add_plant(plant)
    print(f"Добавлено {len(collection)} растений.")
    print()

    # Полив
    today = date.today()
    collection.water_plant(plants[0], today)
    collection.water_plant(plants[1], today)
    print(f"Поливаем {today.strftime('%d.%m.%Y')}:")
    for p in plants:
        print(f"  {p.name}: {'полит' if p.last_watered == today else 'не полит'}")
    print()

    # Пересадки
    new_date = today + timedelta(days=7)
    collection.repot_plant(plants[2], new_date)
    print(f"Пересаживаем {new_date.strftime('%d.%m.%Y')}:")
    for p in plants:
        print(f"  {p.name}: {'пересажен' if p.last_repotted == new_date else 'не пересажен'}")
    print()

    # Заметки
    note = Note("Урожай помидоров будет через 30 дней", date.today())
    collection.add_note(note)
    print(f"Заметка: {note.text}")
    print()

    # Напоминания
    reminder = Reminder("Проверить почву у базилика", date.today() + timedelta(days=2))
    collection.add_reminder(reminder)
    print(f"Напоминание: {reminder.text} ({reminder.date.strftime('%d.%m.%Y')})")
    print()

    # Статистика
    print("=== Статистика ===")
    print(f"Всего растений: {collection.get_plant_count()}")
    print(f"Всего поливов: {collection.get_water_count()}")
    print(f"Всего пересадок: {collection.get_repot_count()}")
    print(f"Всего заметок: {collection.get_note_count()}")
    print(f"Всего напоминаний: {collection.get_reminder_count()}")
    print()

    # Вывод всех записей
    print("=== Все записи ===")
    for entry in collection.get_entries():
        print(entry)
    print()
    print("=== Demo завершён ===")
