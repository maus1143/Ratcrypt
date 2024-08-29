import os
import time

def xor_encrypt(plain_text, key):
    key = key.encode()
    key_len = len(key)
    encrypted_chars = []

    for i, char in enumerate(plain_text):
        key_char = key[i % key_len]
        encrypted_char = chr(ord(char) ^ key_char)
        encrypted_chars.append(encrypted_char)

    encrypted_text = ''.join(encrypted_chars)
    return encrypted_text

def main():
    try:
        # Eingabe des Klartexts und des XOR-Schlüssels
        plain_text = input("Geben Sie den zu verschlüsselnden Text ein: ")
        xor_key = input("Geben Sie den XOR-Schlüssel ein (ein beliebiges Passwort): ")

        # XOR-Verschlüsselung des Klartexts
        encrypted_text = xor_encrypt(plain_text, xor_key)

        # Pfad zur Datei 'encrypted_data.txt' im gleichen Verzeichnis wie das Skript
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "Verschlüsselt.txt")

        # Schreiben der verschlüsselten Daten in die Datei
        with open(file_path, "w") as file:
            file.write(f"{encrypted_text}\n")

        print(f"Verschlüsselte Daten wurden in '{file_path}' gespeichert.")
        time.sleep(20)

    except Exception as e:
        print(f"Fehler beim Verschlüsseln: {e}")
        time.sleep(20)

if __name__ == "__main__":
    main()
