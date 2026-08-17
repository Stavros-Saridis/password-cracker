import itertools
import string
import threading
from src.hasher import hash_password

found_password = None
found_lock = threading.Lock()

def brute_force_worker(target_hash, algorithm, candidates, result):
    global found_password
    for candidate in candidates:
        if found_password:
            return
        candidate_hash = hash_password(candidate, algorithm)
        if candidate_hash == target_hash:
            with found_lock:
                found_password = candidate
                result.append(candidate)
            return

def brute_force(target_hash, algorithm, max_length=6, charset=None, threads=4):
    global found_password
    found_password = None

    if charset is None:
        charset = string.ascii_lowercase + string.digits

    print(f"[*] Starting brute force attack...")
    print(f"[*] Charset: {charset}")
    print(f"[*] Max length: {max_length}")
    print(f"[*] Threads: {threads}")

    attempts = 0
    result = []

    for length in range(1, max_length + 1):
        if found_password:
            break

        print(f"[*] Trying length {length}...")
        all_candidates = list(itertools.product(charset, repeat=length))
        candidates_str = [''.join(c) for c in all_candidates]
        attempts += len(candidates_str)

        chunk_size = max(1, len(candidates_str) // threads)
        chunks = [candidates_str[i:i+chunk_size] for i in range(0, len(candidates_str), chunk_size)]

        thread_list = []
        for chunk in chunks:
            t = threading.Thread(target=brute_force_worker, args=(target_hash, algorithm, chunk, result))
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join()

        if found_password:
            break

    if found_password:
        print(f"\n[+] PASSWORD FOUND!")
        print(f"[+] Password: {found_password}")
        print(f"[+] Attempts: {attempts:,}")
        return found_password

    print(f"[-] Password not found after {attempts:,} attempts.")
    return None