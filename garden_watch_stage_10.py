# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GardenWatch
def export_to_json():
    import json
    from datetime import datetime
    
    data = {
        "plants": {},
        "last_updated": datetime.now().isoformat()
    }
    
    for plant_id, details in _plant_registry.items():
        if not isinstance(details, dict):
            continue
            
        record = {
            "name": details.get("name", ""),
            "type": details.get("type", ""),
            "last_watered": details.get("last_watered"),
            "next_watering": details.get("next_watering"),
            "notes": details.get("notes", []),
            "transfers": details.get("transfers", [])
        }
        
        if record["name"]:
            data["plants"][record["name"]] = record
            
    return json.dumps(data, ensure_ascii=False, indent=2)
