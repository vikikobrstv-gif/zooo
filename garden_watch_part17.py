# === Stage 17: Добавь группировку записей по категориям ===
# Project: GardenWatch
def group_by_category(records):
    categories = {}
    for record in records:
        cat = record.get('category', 'General')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(record)
    return list(categories.items())
