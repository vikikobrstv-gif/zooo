# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GardenWatch
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    
    if not records:
        return []
    
    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # Понедельник текущей недели
    week_end = week_start + timedelta(days=6)
    
    weekly_data = {
        'week_start': week_start,
        'watering_count': 0,
        'transplant_count': 0,
        'notes_count': 0,
        'plants_affected': set()
    }
    
    for record in records:
        if record['date'] >= week_start and record['date'] <= week_end:
            action = record.get('action', '').lower()
            
            if action == 'watering':
                weekly_data['watering_count'] += 1
            elif action == 'transplant':
                weekly_data['transplant_count'] += 1
            
            note_text = record.get('note', '')
            if note_text.strip():
                weekly_data['notes_count'] += 1
            
            plant_name = record.get('plant')
            if plant_name:
                weekly_data['plants_affected'].add(plant_name)
    
    return [weekly_data]
