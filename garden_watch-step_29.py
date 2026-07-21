# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GardenWatch
def load_config():
    config = {
        "app_name": "GardenWatch",
        "version": 1,
        "language": "ru",
        "theme": {
            "primary_color": "#2e7d32",
            "bg_color": "#f5f5f5",
            "text_color": "#212121"
        },
        "logging": {
            "level": "INFO",
            "file": "gardenwatch.log"
        },
        "max_notes_per_day": 3,
        "default_water_interval_hours": 48,
        "notification_sound": "chime.wav",
        "data_dir": ".gardenwatch_data",
        "features": {
            "reminders": True,
            "photos": False,
            "ai_assistant": False
        }
    }
    return config

def save_config(config):
    with open("config.json", "w") as f:
        import json
        json.dump(config, f, indent=2)
