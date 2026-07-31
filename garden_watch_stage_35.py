# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GardenWatch
def get_next_action(plants, now):
    """Returns a list of recommended actions for the garden."""
    actions = []
    watered = {p["name"]: p.get("last_water", 0) for p in plants}
    transplanted = {p["name"]: p.get("last_transplant", 0) for p in plants}
    
    for plant in plants:
        name = plant["name"]
        needs_water = now - watered[name] > 3 # days
        if needs_water:
            actions.append(f"{name}: полить")
        
        needs_transplant = now - transplanted[name] > 60
        if needs_transplant:
            actions.append(f"{name}: пересадить")
    
    notes = {p["name"]: p.get("last_note", 0) for p in plants}
    for plant in plants:
        name = plant["name"]
        last_note = notes[name]
        if now - last_note > 7 and plant.get("needs_attention"):
            actions.append(f"{name}: обратить внимание")
    
    return actions
