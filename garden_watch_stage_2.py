# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GardenWatch
class Plant:
    def __init__(self, name, water_days=0, last_water=None):
        self.name = name
        self.water_days = water_days
        self.last_water = last_water

def validate_input(user_input):
    if not user_input.strip():
        return None, "Ввод пустой"
    parts = user_input.split(maxsplit=1)
    if len(parts) < 2:
        return None, "Не хватает данных (имя и действие)"
    name, action = parts
    valid_actions = {"water", "note", "move"}
    if action.lower() not in valid_actions:
        return None, f"Неизвестное действие. Допустимы: {', '.join(valid_actions)}"
    if len(name) < 2 or len(name) > 50:
        return None, "Имя растения должно быть от 2 до 50 символов"
    return name, action
