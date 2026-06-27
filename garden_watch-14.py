# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GardenWatch
def generate_summary(data):
    today = datetime.date.today()
    summary_lines = ["=== GardenWatch Daily Summary ===", f"Date: {today.strftime('%Y-%m-%d')}", ""]
    
    plants_needing_water = [p for p in data['plants'] if p.get('last_watered', None) and (today - datetime.date.fromisoformat(p['last_watered'])).days >= 7]
    summary_lines.append(f"Plants needing water: {len(plants_needing_water)}")
    
    recent_transplants = [p for p in data['plants'] if p.get('transplanted_date') and (today - datetime.date.fromisoformat(p['transplanted_date'])).days <= 30]
    summary_lines.append(f"Recently transplanted: {len(recent_transplants)}")
    
    total_notes = len(data.get('notes', []))
    summary_lines.append(f"Total notes: {total_notes}")
    
    if data.get('reminders'):
        due_reminders = [r for r in data['reminders'] if datetime.date.fromisoformat(r['date']) == today]
        summary_lines.append(f"Reminders due today: {len(due_reminders)}")
        
    summary_text = "\n".join(summary_lines)
    
    print(summary_text)
