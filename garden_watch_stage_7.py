# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GardenWatch
def sort_records(records, key='date'):
    if not records: return []
    reverse = False
    if key == 'priority':
        def _sort_r(r): return -r.get('priority', 0)
        reverse = True
    elif key == 'name':
        def _sort_r(r): return r.get('name', '').lower()
    else: # date (default)
        def _sort_r(r): return r.get('date') or ''
    return sorted(records, key=_sort_r, reverse=reverse)
