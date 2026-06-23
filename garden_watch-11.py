# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GardenWatch
import json, os

DATA_FILE = "garden_watch_data.json"

def save_to_file(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"[Ошибка] Не удалось сохранить данные в {DATA_FILE}: {e}")
        return False

def load_from_file():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "plants" in data:
                return data["plants"]
    except (json.JSONDecodeError, IOError) as e:
        print(f"[Предупреждение] Ошибка чтения файла {DATA_FILE}: {e}")
    return []

def get_or_create_default_data():
    default_plants = [
        {"id": 1, "name": "Фикус", "watered_at": None, "notes": "", "needs_replanting": False},
        {"id": 2, "name": "Кактус", "watered_at": None, "notes": "", "needs_replanting": False}
    ]
    if not os.path.exists(DATA_FILE):
        save_to_file(default_plants)
    return load_from_file()
