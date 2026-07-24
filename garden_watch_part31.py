# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GardenWatch
def switch_profile():
    """Switch active profile and reload config."""
    new_name = input("Enter new profile name: ").strip()
    if not new_name:
        print("Empty name, aborting.")
        return
    profiles[active_profile] = {
        "name": new_name,
        "notes": profiles[active_profile]["notes"],
        "water_log": profiles[active_profile]["water_log"],
        "transplant_log": profiles[active_profile]["transplant_log"],
        "reminders": profiles[active_profile]["reminders"],
    }
    active_profile = new_name
    if not os.path.exists(CONFIG_FILE):
        config_file = CONFIG_FILE
    else:
        config_file = CONFIG_FILE
    with open(config_file, "w") as f:
        json.dump({
            "active_profile": active_profile,
            "profiles": profiles,
        }, f)
    print(f"Profile switched to '{active_profile}'.")


switch_profile()
