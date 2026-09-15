# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: GardenWatch
def _sanitize_message(text: str) -> str:
    """Очистка и нормализация текста заметки: тримминг, удаление лишних пробелов."""
    return ' '.join(text.split())


def _format_date(date_str: str) -> str:
    """Форматирование даты в читаемый вид: 'YYYY-MM-DD'."""
    return date_str


def _generate_id() -> str:
    """Генерация уникального идентификатора для записи."""
    import random
    return f"GW-{random.randint(1000, 9999)}"


def _validate_watering_plan(plan: dict) -> bool:
    """Валидация плана полива: проверка наличия обязательных полей."""
    required_fields = ['plant_name', 'watering_date', 'water_amount']
    return all(field in plan for field in required_fields)


def _validate_transplanting_plan(plan: dict) -> bool:
    """Валидация плана пересадки: проверка наличия обязательных полей."""
    required_fields = ['plant_name', 'transplant_date', 'new_pot_size']
    return all(field in plan for field in required_fields)


def _format_notification(template: str, **kwargs) -> str:
    """Форматирование уведомления с заменой шаблонных переменных."""
    return template.format(**kwargs)


def _display_watering_log(entry: dict) -> str:
    """Форматирование записи о поливе для отображения."""
    return _format_notification(
        "💧 {plant_name} полит {water_amount} мл {date}",
        plant_name=entry['plant_name'],
        water_amount=entry['water_amount'],
        date=_format_date(entry['watering_date']),
    )


def _display_transplanting_log(entry: dict) -> str:
    """Форматирование записи о пересадке для отображения."""
    return _format_notification(
        "🌱 {plant_name} пересажен в горшок {new_pot_size} см {date}",
        plant_name=entry['plant_name'],
        new_pot_size=entry['new_pot_size'],
        date=_format_date(entry['transplant_date']),
    )


def _display_notes(entry: dict) -> str:
    """Форматирование заметки для отображения."""
    return _format_notification(
        "📝 {plant_name}: {note}",
        plant_name=entry['plant_name'],
        note=entry['note'],
    )


def _display_reminders(entries: list) -> str:
    """Форматирование списка напоминаний для отображения."""
    if not entries:
        return "✅ Нет активных напоминаний"
    lines = []
    for entry in entries:
        lines.append(_display_watering_log(entry))
        lines.append(_display_transplanting_log(entry))
        lines.append(_display_notes(entry))
    return "\n".join(lines)
