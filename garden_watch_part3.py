# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GardenWatch
class GardenWatch:
    def __init__(self):
        self.records = []
        self.reminders = {}

    def add_watering(self, plant_name, date=None, note=""):
        if not date:
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        record = {
            "type": "watering",
            "plant": plant_name,
            "date": date,
            "note": note
        }
        self.records.append(record)
        print(f"Запись о поливе '{plant_name}' от {date} добавлена.")

    def add_transplant(self, plant_name, old_soil, new_soil, date=None, note=""):
        if not date:
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        record = {
            "type": "transplant",
            "plant": plant_name,
            "old_soil": old_soil,
            "new_soil": new_soil,
            "date": date,
            "note": note
        }
        self.records.append(record)
        print(f"Запись о пересадке '{plant_name}' от {date} добавлена.")

    def add_note(self, plant_name, text, date=None):
        if not date:
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        record = {
            "type": "note",
            "plant": plant_name,
            "text": text,
            "date": date
        }
        self.records.append(record)
        print(f"Заметка для '{plant_name}' от {date} сохранена.")

    def add_reminder(self, plant_name, event_type, target_date):
        if not isinstance(target_date, str):
            from datetime import datetime
            target_date = target_date.strftime("%Y-%m-%d")
        self.reminders[plant_name] = {
            "event": event_type,
            "date": target_date
        }
        print(f"Напоминание для '{plant_name}' ({event_type}) на {target_date} установлено.")

    def get_plant_history(self, plant_name):
        return [r for r in self.records if r["plant"] == plant_name]
