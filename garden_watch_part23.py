# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GardenWatch
def print_report(plants, logs):
    """Compact console report: status table + recent log summary."""
    print(f"\n{'='*50}")
    print("  GARDENWATCH — Status Report")
    print(f"{'='*50}")
    
    # Group by plant name for the table
    rows = []
    for p in plants:
        last_log = next((l for l in logs if l.plant == p), None)
        status = "OK" if last_log else "No log"
        rows.append([p.name, last_log.watered or "", last_log.transplanted or "", status])

    # Print header with alignment
    widths = [5, 12, 15, 8]
    headers = ["Plant", "Last watered", "Transplanted", "Status"]
    
    # Calculate dynamic column widths if names are longer
    for i in range(4):
        max_w = widths[i]
        for row in rows:
            w = len(str(row[i]))
            if w > max_w and i == 0:
                widths[i] = w
    
    print(f"{'Plant':<{widths[0]}} {'Last watered':<{widths[1]}} {'Transplanted':<{widths[2]}} {'Status':<{widths[3]}}")
    
    # Print separator line
    sep = "".join("-" * w for w in widths)
    print(sep)
    
    # Print each row
    for row in rows:
        print(f"{row[0]:<{widths[0]}} {row[1]:<{widths[1]}} {row[2]:<{widths[2]}} {row[3]:<{widths[3]}}")
    
    # Print recent log summary (last 5 entries)
    print(f"\n{'-'*50}")
    print("  Recent Activity Log:")
    for log in logs[-5:]:
        action = "Watered" if log.action == "water" else ("Transplanted" if log.action == "transplant" else log.action.capitalize())
        print(f"  [{log.date}] {action}: {log.plant.name} — Note: {log.note}")
    
    print(f"\n{'='*50}\n")
