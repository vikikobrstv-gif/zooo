# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GardenWatch
import json, sys, os, datetime as dt

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
    
    if not isinstance(data, dict):
        print("JSON должен содержать объект (словарь).")
        return {}

    # Нормализация дат в ISO-формат для удобства работы с datetime
    def normalize_date(date_str):
        try:
            dt_obj = dt.datetime.fromisoformat(date_str)
            return dt_obj.strftime("%Y-%m-%d %H:%M") if date_str else None
        except (ValueError, TypeError):
            return None

    # Обработка списка растений
    plants_list = data.get("plants", [])
    if isinstance(plants_list, list):
        for plant in plants_list:
            if not isinstance(plant, dict): continue
            if "name" in plant and not isinstance(plant["name"], str): continue
            
            # Обработка истории ухода (полив, пересадка)
            care_history = plant.get("care", [])
            if isinstance(care_history, list):
                for entry in care_history:
                    if isinstance(entry, dict) and "date" in entry:
                        entry["date"] = normalize_date(entry["date"])

    # Обработка напоминаний (задач)
    tasks_list = data.get("tasks", [])
    if isinstance(tasks_list, list):
        for task in tasks_list:
            if not isinstance(task, dict): continue
            if "title" in task and not isinstance(task["title"], str): continue
            
            # Обработка даты напоминания
            due_date = task.get("due", {})
            if isinstance(due_date, dict) and "date" in due_date:
                task["due"] = normalize_date(due_date["date"])

    return data
