# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GardenWatch
def parse_date(date_str):
    """Парсит дату 'DD.MM.YYYY' или 'YYYY-MM-DD', возвращает datetime.date."""
    import datetime
    date_str = date_str.strip()
    for fmt in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Некорректный формат даты: '{date_str}'. Используйте DD.MM.YYYY или YYYY-MM-DD.")

def format_date(dt):
    """Форматирует дату в DD.MM.YYYY."""
    if isinstance(dt, datetime.datetime):
        dt = dt.date()
    return f"{dt.day}.{dt.month}.{dt.year}"
