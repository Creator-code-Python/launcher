import json
import os

CONFIG_FILE = "config.json"

def load():
    if not os.path.exists(CONFIG_FILE):
        return {"files": [], "gui": {}}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_file():
    data = load()
    name = input("Название файла: ")
    filename = input("Имя файла: ")
    url = input("URL: ")
    data["files"].append({
        "name": name,
        "filename": filename,
        "url": url
    })
    save(data)
    print("[✓] Файл добавлен!")

def set_gui():
    data = load()
    name = input("Название GUI: ")
    filename = input("Имя файла: ")
    url = input("URL: ")
    data["gui"] = {
        "name": name,
        "filename": filename,
        "url": url
    }
    save(data)
    print("[✓] GUI обновлён!")

def menu():
    while True:
        print("\n=== UPLOADER ===")
        print("1. Добавить файл")
        print("2. Обновить GUI")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            add_file()
        elif choice == "2":
            set_gui()
        elif choice == "0":
            break

menu()
