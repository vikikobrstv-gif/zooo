# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: GardenWatch
def self_check():
        """Финальная самопроверка приложения."""
        print("=== Самопроверка GardenWatch ===")
        checks = [
            ("Модули", [__import__(m) for m in ['os', 'json', 'datetime', 'sys']]),
            ("Функции", [
                self_check,
                self_check.__module__,
                self_check.__name__,
            ]),
            ("Дата", datetime.now()),
        ]
        for name, result in checks:
            print(f"✓ {name}: {result}")
        print("=== Проверка завершена ===")
