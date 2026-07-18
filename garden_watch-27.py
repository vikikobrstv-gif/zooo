# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GardenWatch
def reset_demo_data():
    """Reset all internal state to a fresh demo dataset."""
    global plants, logs, reminders
    plants = [
        {"id": 1, "name": "Роза", "species": "Rosa", "watered_on": None, "notes": "Нужен полив."},
        {"id": 2, "name": "Мята", "species": "Mentha", "watered_on": None, "notes": ""},
        {"id": 3, "name": "Бальзамин", "species": "Impatiens", "watered_on": None, "notes": ""},
    ]
    logs = []
    reminders = []

def clear_state():
    """Remove all data: plants, logs, and reminders."""
    global plants, logs, reminders
    plants.clear()
    logs.clear()
    reminders.clear()
