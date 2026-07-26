# === Stage 32: Добавь журнал действий пользователя ===
# Project: GardenWatch
import json
from datetime import datetime, timezone


class ActionLog:
    """Журнал действий пользователя: полив, пересадка, заметки."""

    def __init__(self):
        self.log = []

    def record(self, action_type: str, plant_name: str, details: dict = None):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "type": action_type,
            "plant": plant_name,
            "details": details or {},
        }
        self.log.append(entry)

    def get_actions(self, since: str = None):
        actions = self.log
        if since:
            actions = [a for a in actions if a["timestamp"] >= since]
        return actions

    @staticmethod
    def load(path="actions.json"):
        try:
            with open(path, "r") as f:
                data = json.load(f)
            log = ActionLog()
            log.log = data.get("entries", [])
            return log
        except FileNotFoundError:
            return ActionLog()

    def save(self, path="actions.json"):
        with open(path, "w") as f:
            json.dump({"entries": self.log}, f)


log = ActionLog.load()


def add_action(action_type, plant_name, details=None):
    log.record(action_type, plant_name, details or {})
