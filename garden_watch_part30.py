# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GardenWatch
class Profile:
    def __init__(self, name: str = "Default", notes: dict | None = None):
        self.name = name
        self.notes = notes or {}

    def add_note(self, key: str, value: str) -> None:
        self.notes[key] = value

    def get_note(self, key: str) -> str | None:
        return self.notes.get(key)


class ProfileManager:
    _profiles: dict[str, Profile] = {}

    @classmethod
    def register(cls, profile: Profile) -> None:
        cls._profiles[profile.name] = profile

    @classmethod
    def get_profile(cls, name: str | int) -> Profile:
        if isinstance(name, int):
            return list(cls._profiles.values())[name % len(cls._profiles)]
        return cls._profiles[name]

    @classmethod
    def add_note_for_profile(cls, profile_name: str, key: str, value: str) -> None:
        prof = cls.get_profile(profile_name)
        prof.add_note(key, value)

    @classmethod
    def get_notes_for_profile(cls, profile_name: str) -> dict[str, str]:
        return dict(getattr(cls._profiles[profile_name], "notes"))


register(Profile("Default", {"water_reminder": "08:00", "plant_count": "5"}))
register(Profile("Gardener", {"water_reminder": "07:30", "plant_count": "12", "favorite_plant": "Tomato"}))
