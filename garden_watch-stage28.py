# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GardenWatch
def project_metrics():
    """Подсчёт ключевых метрик проекта GardenWatch."""
    with open("garden_watch.py", "r", encoding="utf-8") as f:
        code = f.read()
    
    total_lines = len(code.splitlines())
    imports = [l for l in code.splitlines() if l.strip().startswith(("import ", "from "))]
    functions = [l for l in code.splitlines() if l.strip().startswith("def ") and not l.strip().startswith("def project_metrics")]
    classes = [l for l in code.splitlines() if l.strip().startswith("class ")]
    
    print(f"Всего строк: {total_lines}")
    print(f"Импорты (без stdlib): {len(imports)}")
    print(f"Функции: {len(functions)}")
    print(f"Классы: {len(classes)}")
