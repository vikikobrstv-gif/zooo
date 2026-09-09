# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GardenWatch
def migrate_structure(new_version, old_structure):
    """
    Миграция структуры данных при увеличении версии.
    
    new_version: новая версия структуры
    old_structure: текущая структура данных
    
    Возвращает новую структуру с применёнными миграциями.
    """
    if new_version == 1:
        # Базовая структура: список записей ухода
        return {
            "records": [],
            "plant_names": set()
        }
    elif new_version == 2:
        # Добавляем поле "priority" для напоминаний
        if "records" in old_structure:
            for record in old_structure["records"]:
                if "priority" not in record:
                    record["priority"] = "normal"
        return old_structure
    elif new_version == 3:
        # Добавляем индексирование по дате
        if "records" in old_structure:
            indexed_records = []
            for record in old_structure["records"]:
                indexed_records.append({
                    "date": record.get("date", "2024-01-01"),
                    "action": record.get("action", "unknown"),
                    "plant": record.get("plant", "unknown"),
                    "notes": record.get("notes", ""),
                    "priority": record.get("priority", "normal"),
                    "id": record.get("id", len(indexed_records) + 1)
                })
            return {
                "records": indexed_records,
                "plant_names": old_structure.get("plant_names", set()),
                "index": {r["id"]: r for r in indexed_records}
            }
    elif new_version == 4:
        # Добавляем метаданные и статистику
        if "records" in old_structure:
            stats = {
                "total_actions": len(old_structure["records"]),
                "unique_plants": len(old_structure.get("plant_names", set())),
                "last_migration": "2024-01-01"
            }
            return {
                **old_structure,
                "metadata": stats
            }
    else:
        return old_structure
