import os
import time

def xor_decrypt(encrypted_text, key):
    try:
        key = key.encode()
        key_len = len(key)
        decrypted_chars = []
        
        for i, char in enumerate(encrypted_text):
            key_char = key[i % key_len]
            decrypted_char = chr(ord(char) ^ key_char)
            decrypted_chars.append(decrypted_char)
        
        decrypted_text = ''.join(decrypted_chars)
        return decrypted_text
    
    except Exception as e:
        return f"Fehler beim XOR-Entschlüsseln: {e}"

def main():
    try:
        # Pfad zur Datei 'Verschlüsselt.txt'
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "Verschlüsselt.txt")
        print(f"Pfad zur Datei: {file_path}")

        # Daten aus der Datei lesen
        with open(file_path, "r") as file:
            encrypted_text = file.read().strip()

        # Benutzereingabe des XOR-Schlüssels
        xor_key = input("Geben Sie den XOR-Schlüssel ein: ").strip()

        # XOR entschlüsseln
        decrypted_text = xor_decrypt(encrypted_text, xor_key)

        print(f"Entschlüsselter Text: {decrypted_text}")
        time.sleep(20)

    except Exception as e:
        print(f"Fehler beim Entschlüsseln: {e}")
        time.sleep(20)

if __name__ == "__main__":
    main()
# by Mausi :3