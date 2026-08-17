import itertools
import string
from src.hasher import hash_password

def brute_force(target_hash, algorithm, max_length=6, charset=None):
    if charset is None:
        charset = string.ascii_lowercase + string.digits

    print(f"[*] Starting brute force attack...")
    print(f"[*] Charset: {charset}")
    print(f"[*] Max length: {max_length}")

    attempts = 0

    for length in range(1, max_length + 1):
        print(f"[*] Trying length {length}...")
        for combo in itertools.product(charset, repeat=length):
            candidate = ''.join(combo)
            candidate_hash = hash_password(candidate, algorithm)
            attempts += 1

            if attempts % 100000 == 0:
                print(f"[*] Attempts: {attempts:,} — current: {candidate}")

            if candidate_hash == target_hash:
                print(f"\n[+] PASSWORD FOUND!")
                print(f"[+] Password: {candidate}")
                print(f"[+] Attempts: {attempts:,}")
                return candidate

    print(f"[-] Password not found after {attempts:,} attempts.")
    return None