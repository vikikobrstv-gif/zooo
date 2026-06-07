# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GardenWatch
import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = "garden_data.json"

def load_data():
    if not Path(DATA_FILE).exists():
        return {
            "plants": [
                {"name": "Томат", "watered": False, "last_water": None, "notes": "Любит солнце"},
                {"name": "Бальзамин", "watered": True, "last_water": datetime.now().isoformat(), "notes": "В тени"}
            ],
            "tasks": [
                {"id": 1, "text": "Поливать томаты", "done": False},
                {"id": 2, "text": "Пересадить фикус", "done": True}
            ]
        }
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    data = load_data()
    print("Добро пожаловать в GardenWatch!")
    for plant in data["plants"]:
        status = "полив" if not plant["watered"] else "не требует полива"
        print(f'{plant["name"]}: {status}')

if __name__ == "__main__":
    main()
