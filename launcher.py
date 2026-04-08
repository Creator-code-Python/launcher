import os
import urllib.request
import json

CONFIG_URL = "https://raw.githubusercontent.com/yourname/repo/main/config.json"
INSTALL_DIR = os.path.join(os.path.expanduser("~"), "MyLauncher")
os.makedirs(INSTALL_DIR, exist_ok=True)

def load_config():
    try:
        with urllib.request.urlopen(CONFIG_URL) as response:
            return json.loads(response.read().decode())
    except:
        print("[!] Ошибка загрузки конфигурации")
        return None

def download(file):
    try:
        path = os.path.join(INSTALL_DIR, file["filename"])
        print(f"[+] Скачивание {file['name']}...")
        urllib.request.urlretrieve(file["url"], path)
        print(f"[✓] Установлено: {path}")
    except Exception as e:
        print(f"[!] Ошибка: {e}")

def submenu(files_list):
    while True:
        print("\n--- Выберите что скачивать ---")
        for i, f in enumerate(files_list, start=1):
            print(f"{i}. {f['name']}")
        print("0. Назад")

        choice = input("Выбор: ")
        if choice == "0":
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(files_list):
                download(files_list[choice - 1])
            else:
                print("Неверный выбор!")
        except:
            print("Ошибка ввода!")

def menu():
    while True:
        config = load_config()
        if not config:
            return

        print("\n=== LAUNCHER ===")
        print("1. Скачать CFG")
        print("2. Скачать Skin")
        print("3. Скачать GUI")
        print("9. Скачать всё")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "0":
            break
        elif choice == "1":
            cfg_files = [f for f in config["files"] if "cfg" in f["filename"].lower()]
            submenu(cfg_files)
        elif choice == "2":
            skin_files = [f for f in config["files"] if "skin" in f["filename"].lower()]
            submenu(skin_files)
        elif choice == "3":
            submenu([config["gui"]])
        elif choice == "9":
            for f in config["files"]:
                download(f)
            download(config["gui"])
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()
