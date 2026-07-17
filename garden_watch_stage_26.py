# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GardenWatch
def demo():
    print("=== GardenWatch Demo ===")
    plant = {"id": 1, "name": "Роза", "needs_watering": True}
    log_entry = {"date": "2024-06-15", "action": "watered", "notes": "Добавил удобрения"}
    print(f"Plant: {plant['id']}, {plant['name']}")
    print(f"Log entry: {log_entry}")
