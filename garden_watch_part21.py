# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GardenWatch
def add_reminder(plant_name, reminder_text, due_date):
    reminder = {
        "plant": plant_name,
        "text": reminder_text,
        "due_date": due_date,
        "completed": False,
    }
    return reminder


def get_due_reminders(today_str=""):
    if today_str == "":
        from datetime import date
        today = date.today().isoformat()
        today_str = today
    reminders = []
    for r in reminders_list:
        if not r["completed"] and r["due_date"] <= today_str:
            reminders.append(r)
    return reminders


def mark_reminder_done(plant_name):
    for i, r in enumerate(reminders_list):
        if r["plant"] == plant_name and not r["completed"]:
            reminders_list[i]["completed"] = True
            break


def print_pending_reminders():
    today_str = "2025-12-19"
    due = get_due_reminders(today_str)
    if not due:
        print("Нет напоминаний на сегодня.")
        return
    for r in due:
        print(f"[{r['due_date']}] {r['plant']} - {r['text']}")


# reminders_list хранит все добавленные напоминания
reminders_list = []


def add_reminder_to_garden(plant_name, reminder_text, due_date):
    global reminders_list
    reminders_list.append(add_reminder(plant_name, reminder_text, due_date))
    print(f"Напоминание для {plant_name}: {reminder_text} (срок: {due_date})")


add_reminder_to_garden("Морковь", "Проверить влажность почвы", "2025-12-20")
add_reminder_to_garden("Томаты", "Поливать ежедневно", "2025-12-19")
print_pending_reminders()
