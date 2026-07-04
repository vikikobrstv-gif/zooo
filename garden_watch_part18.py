# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GardenWatch
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name):
        if not any(t['name'] == name for t in self.db.get('tags', [])):
            self.db.setdefault('tags', []).append({'id': len(self.db.get('tags', [])) + 1, 'name': name})
    
    def remove_tag(self, tag_name):
        tags = self.db.get('tags', [])
        for i in range(len(tags) - 1, -1, -1):
            if tags[i]['name'] == tag_name:
                del tags[i]
                return True
        return False
    
    def add_tag_to_plant(self, plant_id, tag_name):
        plants = self.db.get('plants', [])
        for i in range(len(plants) - 1, -1, -1):
            if plants[i]['id'] == plant_id:
                tags_list = plants[i].setdefault('tags', [])
                existing_tags = [t['name'] for t in tags_list]
                if tag_name not in existing_tags and self.db.get('tags'):
                    matching_tag = next((t for t in self.db['tags'] if t['name'] == tag_name), None)
                    if matching_tag:
                        tags_list.append({'id': matching_tag['id'], 'name': tag_name})
                return True
        return False
    
    def remove_tag_from_plant(self, plant_id, tag_name):
        plants = self.db.get('plants', [])
        for i in range(len(plants) - 1, -1, -1):
            if plants[i]['id'] == plant_id:
                tags_list = plants[i].get('tags', [])
                filtered_tags = [t for t in tags_list if t['name'] != tag_name]
                if len(filtered_tags) < len(tags_list):
                    plants[i]['tags'] = filtered_tags
                    return True
        return False
