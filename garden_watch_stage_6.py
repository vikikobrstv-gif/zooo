# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GardenWatch
class GardenFilter:
    def __init__(self, records):
        self.records = records
    
    def filter_by_status(self, status=None):
        if not status:
            return list(self.records)
        return [r for r in self.records if r.get('status') == status]
    
    def filter_by_category(self, category=None):
        if not category:
            return list(self.records)
        return [r for r in self.records if r.get('category') == category]
    
    def filter_by_tag(self, tag=None):
        if not tag:
            return list(self.records)
        return [r for r in self.records if any(tag.lower() in t.lower() for t in r.get('tags', []))]
    
    def combine_filters(self, status=None, category=None, tags=None):
        filtered = self.filter_by_status(status)
        filtered = self.filter_by_category(category, records=filtered)
        filtered = self.filter_by_tag(tags, records=filtered)
        return filtered
