# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GardenWatch
import os, json, shutil
from datetime import datetime

def backup_data(data_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"gardenwatch_{timestamp}.json"
    backup_path = os.path.join(backup_dir, backup_name)
    if os.path.exists(data_path):
        shutil.copy2(data_path, backup_path)
        print(f"✅ Резервная копия: {backup_path}")
    else:
        print("⚠️ Файл данных не найден, резервная копия не создана.")
    return backup_path
