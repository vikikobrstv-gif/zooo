# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GardenWatch
def check_overdue_reminders():
    now = datetime.now()
    overdue = []
    for item in reminders:
        if item["time"] and isinstance(item["time"], datetime):
            if now > item["time"]:
                overdue.append({"note": item, "delayed_hours": (now - item["time"]).total_seconds() / 3600})
    return overdue

def notify_overdue(overdue_list=None):
    if overdue_list is None:
        overdue_list = check_overdue_reminders()
    for entry in overdue_list:
        print(f"Просрочено напоминание: {entry['note'].get('text', 'Без текста')} (опоздал на {entry['delayed_hours']:.1f} ч.)")

if __name__ == "__main__":
    if reminders:
        overdue = check_overdue_reminders()
        notify_overdue(overdue)
