# === Stage 20: Добавь восстановление записей из архива ===
# Project: GardenWatch
def restore_from_archive():
    """Восстанавливает записи из архива в основной журнал."""
    import json, os, glob
    archive_dir = "archives"
    if not os.path.isdir(archive_dir):
        print("Архив не найден.")
        return
    for f in sorted(glob.glob(os.path.join(archive_dir, "*.json"))):
        with open(f) as fh:
            data = json.load(fh)
        if isinstance(data, list):
            journal.extend(data)
            print(f"Восстановлено {len(data)} записей из {os.path.basename(f)}.")
