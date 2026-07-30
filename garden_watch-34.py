# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GardenWatch
TEMPLATES = [
    {"name": "water",      "template": "[{date}] Полив: {plant} ({amount} мл)"},
    {"name": "transplant", "template": "[{date}] Пересадка: {plant} -> {location}"},
    {"name": "note",       "template": "[{date}] Заметка: {plant}: {text}"},
    {"name": "reminder",  "template": "[{date}] Напоминание: {plant} — {message}"},
]

def new_record(template_name, **kwargs):
    """Создать запись по шаблону."""
    if template_name not in (t["name"] for t in TEMPLATES):
        raise ValueError(f"Неизвестный шаблон: {template_name}. Доступные: {[t['name'] for t in TEMPLATES]}")
    tpl = next(t for t in TEMPLATES if t["name"] == template_name)
    return tpl["template"].format(**kwargs, date=datetime.now().strftime("%Y-%m-%d"))
