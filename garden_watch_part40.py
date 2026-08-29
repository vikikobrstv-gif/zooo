# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GardenWatch
def main():
    parser = argparse.ArgumentParser(description="GardenWatch — журнал ухода за растениями")
    sub = parser.add_subparsers(dest="command", required=True)

    # Команда add
    add_p = sub.add_parser("add", help="Добавить записи")
    add_p.add_argument("--type", choices=["water", "transplant", "note", "reminder"], required=True)
    add_p.add_argument("--plant", required=True)
    add_p.add_argument("--time", default=None, help="Время (HH:MM)")
    add_p.add_argument("--date", default=None, help="Дата (YYYY-MM-DD)")
    add_p.add_argument("--text", default="")
    add_p.add_argument("--id", type=int, default=None, help="ID растения")

    # Команда list
    sub.add_parser("list", help="Показать список записей")

    # Команда delete
    del_p = sub.add_parser("delete", help="Удалить запись")
    del_p.add_argument("--id", type=int, required=True)

    args = parser.parse_args()

    db = load_db()

    if args.command == "add":
        entry = {
            "id": len(db) + 1,
            "type": args.type,
            "plant": args.plant,
            "time": args.time,
            "date": args.date or datetime.now().strftime("%Y-%m-%d"),
            "text": args.text,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        if args.id:
            entry["plant_id"] = args.id
        db.append(entry)
        save_db(db)
        print(f"[OK] Добавлена запись #{entry['id']} — {entry['type']} для {entry['plant']}")

    elif args.command == "list":
        for e in db:
            print(f"[{e['type']}] Растение: {e['plant']} | ID: {e.get('plant_id', '?')} | Время: {e['time']} | Дата: {e['date']} | Текст: {e['text']}")

    elif args.command == "delete":
        db = [e for e in db if e["id"] != args.id]
        save_db(db)
        print(f"[OK] Запись #{args.id} удалена.")

if __name__ == "__main__":
    main()
