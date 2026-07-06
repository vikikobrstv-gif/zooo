# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GardenWatch
def archive_records(records, cutoff_days=365):
    """Archive records older than cutoff_days or marked as completed."""
    archived = []
    for r in records:
        if r.get("completed") and r.get("date"):
            date_str = r["date"][:10]
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d").date()
                today = datetime.today().date()
                if (today - dt).days > cutoff_days:
                    archived.append(r)
            except ValueError:
                pass
        elif r.get("completed"):
            archived.append(r)
    return archived
