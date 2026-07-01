# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GardenWatch
def calculate_monthly_stats(records, year=2024):
    from collections import defaultdict
    stats = defaultdict(lambda: {'watered': 0, 'transplanted': 0, 'notes_count': 0})
    for record in records:
        if isinstance(record['date'], str) and len(record['date']) == 10:
            try:
                date_obj = datetime.strptime(record['date'], '%Y-%m-%d')
                month_key = f"{year}-{date_obj.month}"
                if record.get('action') == 'watered': stats[month_key]['watered'] += 1
                elif record.get('action') == 'transplanted': stats[month_key]['transplanted'] += 1
                else: stats[month_key]['notes_count'] += 1
            except ValueError: pass
    return dict(sorted(stats.items()))
