# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GardenWatch
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query=None, fields=None):
        if not query or not isinstance(query, str) or not query.strip():
            return list(self.data.values())
        
        query_lower = query.lower().strip()
        results = []
        
        for plant_id, record in self.data.items():
            match = False
            
            # Поиск по имени растения (если поле указано или по умолчанию)
            if fields and 'name' in fields:
                if query_lower in str(record.get('name', '')).lower():
                    match = True
            elif not fields or 'name' in fields:
                if query_lower in str(record.get('name', '')).lower():
                    match = True
            
            # Поиск по типу растения (если поле указано)
            if fields and 'type' in fields:
                if query_lower in str(record.get('type', '')).lower():
                    match = True
            elif not fields or 'type' in fields:
                if query_lower in str(record.get('type', '')).lower():
                    match = True
            
            # Поиск по статусу (если поле указано)
            if fields and 'status' in fields:
                if query_lower in str(record.get('status', '')).lower():
                    match = True
            elif not fields or 'status' in fields:
                if query_lower in str(record.get('status', '')).lower():
                    match = True
            
            # Поиск по последней активности (если поле указано)
            if fields and 'last_activity' in fields:
                last_act_str = record.get('last_activity', '')
                if isinstance(last_act_str, datetime):
                    last_act_str = last_act_str.strftime('%Y-%m-%d')
                if query_lower in str(last_act_str).lower():
                    match = True
            elif not fields or 'last_activity' in fields:
                if query_lower in str(record.get('last_activity', '')).lower():
                    match = True
            
            # Поиск по заметкам (если поле указано)
            if fields and 'notes' in fields:
                notes_str = record.get('notes', '')
                if isinstance(notes_str, list):
                    notes_str = ' '.join(str(n) for n in notes_str)
                else:
                    notes_str = str(notes_str)
                if query_lower in notes_str.lower():
                    match = True
            elif not fields or 'notes' in fields:
                notes_str = record.get('notes', '')
                if isinstance(notes_str, list):
                    notes_str = ' '.join(str(n) for n in notes_str)
                else:
                    notes_str = str(notes_str)
                if query_lower in notes_str.lower():
                    match = True
            
            # Поиск по дате полива (если поле указано)
            if fields and 'last_watered' in fields:
                water_date_str = record.get('last_watered', '')
                if isinstance(water_date_str, datetime):
                    water_date_str = water_date_str.strftime('%Y-%m-%d')
                if query_lower in str(water_date_str).lower():
                    match = True
