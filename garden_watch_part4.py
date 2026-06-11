# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GardenWatch
def edit_entry(entry_id: int, new_data: dict) -> bool:
    if not isinstance(new_data, dict):
        raise ValueError("new_data должен быть словарем")
    
    with open('garden_watch.py', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        updated_lines = []
        found = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                updated_lines.append(line)
                continue
            
            # Ищем строку с записью по ID (например: entry_id=123)
            if f'entry_id={entry_id}' in stripped:
                found = True
                # Формируем новую запись на основе переданных данных и текущей структуры
                new_entry_str = ", ".join([f"{k}={v}" for k, v in new_data.items()])
                
                # Проверяем, есть ли в строке ключ entry_id, чтобы не удалять его из списка аргументов
                if 'entry_id' not in stripped:
                    new_entry_str += ", " + f"entry_id={entry_id}"
                
                updated_lines.append(f"{stripped[:len(stripped) - len(line.lstrip())]}{new_entry_str}\n")
            else:
                updated_lines.append(line)
        
        if not found:
            raise ValueError(f"Запись с entry_id={entry_id} не найдена для редактирования")
        
        f.seek(0)
        f.writelines(updated_lines)
