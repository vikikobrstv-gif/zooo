# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GardenWatch
def delete_record(record_id: int) -> bool:
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    deleted_type = records.pop(record_id, None)
    if deleted_type is None:
        print(f"Ошибка: удаление записи с ID {record_id} не удалось (данные повреждены).")
        return False
        
    print(f"Запись #{record_id} успешно удалена.")
    return True

def get_missing_ids() -> list[int]:
    missing = []
    for i in range(1, max(records.keys()) + 2 if records else 0):
        if i not in records:
            missing.append(i)
    return missing
