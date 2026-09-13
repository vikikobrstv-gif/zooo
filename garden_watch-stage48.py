# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: GardenWatch
def parse_date(date_str):
    """Parse date string in YYYY-MM-DD or DD.MM.YYYY format to datetime.date."""
    date_str = date_str.strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.date.fromisoformat(date_str.replace(".", "-"))
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: {date_str}")
