# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GardenWatch
def print_record(record):
    if not record:
        return
    date = record.get("date", "нет даты")
    plant = record.get("plant", "не указано")
    action = record.get("action", "")
    note = record.get("note", "")
    watered = record.get("watered", False)
    repotted = record.get("repotted", False)
    next_water = record.get("next_water", None)
    next_repot = record.get("next_repot", None)

    line = f"[{date}] {plant} — {action}"
    if watered:
        line += " (полив)"
    elif repotted:
        line += " (пересадка)"
    if note.strip():
        line += f" — {note}"
    print(line)

    if next_water and next_repot is None:
        print(f"  → следующий полив: {next_water}")
    elif next_repot and next_water is None:
        print(f"  → следующая пересадка: {next_repot}")
    elif next_water and next_repot:
        print(f"  → полив: {next_water}, пересадка: {next_repot}")

if __name__ == "__main__":
    records = [
        {"date": "2024-01-15", "plant": "Томат 'Детский'", "action": "запись в журнал", "note": "посадил семена"},
        {"date": "2024-01-20", "plant": "Томат 'Детский'", "action": "", "watered": True, "next_water": "2024-01-30"},
        {"date": "2024-02-05", "plant": "Баклажан", "action": "", "repotted": True, "next_repot": "2024-06-05", "note": "пересадил в горшок 15л"},
        {"date": "2024-03-01", "plant": "Огурец", "action": "", "watered": True, "repotted": True, "next_water": "2024-03-10", "next_repot": "2024-07-01"},
        {"date": "2024-05-20", "plant": "Роза садовая", "action": "", "watered": False, "repotted": False},
    ]

    for rec in records:
        print_record(rec)
        print()  # пустая строка между записями
