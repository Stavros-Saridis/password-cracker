from src.hasher import hash_password

def dictionary_attack(target_hash, algorithm, wordlist_path):
    print(f"[*] Starting dictionary attack...")
    print(f"[*] Wordlist: {wordlist_path}")

    attempts = 0

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                candidate = line.strip()
                if not candidate:
                    continue

                candidate_hash = hash_password(candidate, algorithm)
                attempts += 1

                if attempts % 100000 == 0:
                    print(f"[*] Attempts: {attempts:,} — current: {candidate}")

                if candidate_hash == target_hash:
                    print(f"\n[+] PASSWORD FOUND!")
                    print(f"[+] Password: {candidate}")
                    print(f"[+] Attempts: {attempts:,}")
                    return candidate

    except FileNotFoundError:
        print(f"[-] Wordlist not found: {wordlist_path}")
        return None

    print(f"[-] Password not found after {attempts:,} attempts.")
    return None