# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GardenWatch
def load_backup(backup_path):
    """Восстановить данные из текстового резервного файла."""
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Неверный формат резервной копии")
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка解析 резервной копии: {e}")
        return None

def save_backup(data, backup_path):
    """Сохранить данные в текстовый резервный файл."""
    try:
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка сохранения резервной копии: {e}")
        return False

def backup_current_data(backup_path):
    """Создать резервную копию текущих данных."""
    if current_data is None:
        print("Нет данных для резервного копирования")
        return False
    return save_backup(current_data, backup_path)
