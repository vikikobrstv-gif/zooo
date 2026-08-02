# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GardenWatch
def check_integrity_and_repair():
    """Проверяет целостность записей и чинит типичные мелкие проблемы."""
    problems = []
    repaired = 0
    
    for idx, entry in enumerate(entries):
        if not hasattr(entry, 'id'):
            entry.id = f"entry_{idx + 1}"
        
        if not isinstance(entry.date, str) or len(entry.date) < 8:
            problems.append(f"Запись {entry.id}: некорректная дата")
            continue
        
        if not entry.action_type in ['watering', 'repotting', 'note', 'reminder']:
            problems.append(f"Запись {entry.id}: неизвестный тип действия")
        
        if hasattr(entry, 'notes') and (not isinstance(entry.notes, str) or len(str(entry.notes)) < 1):
            entry.notes = ""

    print(f"Проверено записей: {len(entries)}, найдено проблем: {len(problems)}")
