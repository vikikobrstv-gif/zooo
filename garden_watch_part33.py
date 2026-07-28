# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GardenWatch
import sys, os, json, datetime, hashlib, random, shutil, tempfile, textwrap, argparse, base64, uuid, sqlite3, webbrowser, importlib, pathlib, glob, re, math, itertools, collections, logging, time, typing, inspect, subprocess, contextlib

def undo_last(action_type=None):
    journal = load_journal()
    if not journal:
        print("Journal is empty. Nothing to undo.")
        return
    
    log = journal[-1]
    
    if action_type and log.get("type") != action_type:
        print(f"Last entry was '{log.get('type')}', but you asked for type '{action_type}'. Cannot match.")
        return
    
    if not log.get("undone"):
        print("No previous undone state to revert. This is the first undo attempt.")
        return
    
    # Revert: restore old values and remove current entry
    reverted = {
        "id": uuid.uuid4().hex[:8],
        "date": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "action_type": log["type"],
        "details": log["details"],  # keep details intact but mark as undone
        "undone": False,
    }
    
    journal.pop()
    if reverted.get("id"):
        journal.append(reverted)
    
    save_journal(journal)
    print(f"Reverted '{log['type']}' from {log['details']}.")

def load_journal():
    path = os.path.join(BASE_DIR, "gardenwatch", "journal.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path) as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            entries = data.get("entries", [])
            return entries if entries else []
        return []
    except Exception:
        return []

def save_journal(journal):
    path = os.path.join(BASE_DIR, "gardenwatch", "journal.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump({"entries": journal}, f, indent=2, ensure_ascii=False)

# Example usage:
if __name__ == "__main__":
    print("GardenWatch v33 — Undo feature active.")
