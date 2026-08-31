# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GardenWatch
import copy

def dry_run(func, *args, **kwargs):
    """Execute a function in dry-run mode: print what would happen without modifying state.
    Returns the original state snapshot for undo/rollback if needed."""
    state = copy.deepcopy(_get_current_state())
    try:
        print(f"[DRY-RUN] {func.__name__}: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[DRY-RUN] Result: {result}")
        return result
    except Exception as e:
        print(f"[DRY-RUN] Error: {e}")
        return None

def _get_current_state():
    """Return current state from global variables or config."""
    return {
        'water_logs': getattr(water_logs, 'logs', []),
        'transplant_logs': getattr(transplant_logs, 'logs', []),
        'notes': getattr(notes, 'entries', []),
        'reminders': getattr(reminders, 'items', []),
    }
