import json
import os
from src.hasher import hash_password, SUPPORTED_ALGORITHMS

RAINBOW_PATH = os.path.join(os.path.dirname(__file__), '..', 'wordlists', 'rainbow_table.json')

def build_rainbow_table(wordlist_path, algorithms=None, output_path=None):
    if algorithms is None:
        algorithms = ['md5', 'sha1', 'sha256']
    if output_path is None:
        output_path = RAINBOW_PATH

    print(f"[*] Building rainbow table...")
    print(f"[*] Algorithms: {algorithms}")

    table = {}
    count = 0

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue

                for algo in algorithms:
                    h = hash_password(password, algo)
                    table[h] = {'password': password, 'algorithm': algo}

                count += 1
                if count % 10000 == 0:
                    print(f"[*] Processed: {count:,} passwords")

                if count >= 100000:
                    break

    except FileNotFoundError:
        print(f"[-] Wordlist not found: {wordlist_path}")
        return False

    with open(output_path, 'w') as f:
        json.dump(table, f)

    print(f"[+] Rainbow table built — {count:,} passwords, {len(table):,} hashes")
    print(f"[+] Saved to: {output_path}")
    return True

def rainbow_lookup(target_hash, rainbow_path=None):
    if rainbow_path is None:
        rainbow_path = RAINBOW_PATH

    print(f"[*] Looking up hash in rainbow table...")

    try:
        with open(rainbow_path, 'r') as f:
            table = json.load(f)
    except FileNotFoundError:
        print(f"[-] Rainbow table not found. Build it first with --build-rainbow")
        return None

    if target_hash in table:
        result = table[target_hash]
        print(f"\n[+] PASSWORD FOUND!")
        print(f"[+] Password: {result['password']}")
        print(f"[+] Algorithm: {result['algorithm']}")
        return result['password']

    print(f"[-] Hash not found in rainbow table.")
    return None