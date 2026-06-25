# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GardenWatch
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [dict(item) for item in data]
        elif isinstance(data, dict):
            return {k: (list(v) if isinstance(v, list) else v) for k, v in data.items()}
        else:
            print("Ошибка: некорректный формат JSON")
            return []
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{filepath}': {e}")
        return []
