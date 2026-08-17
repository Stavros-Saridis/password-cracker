import itertools
import string
import multiprocessing
from src.hasher import hash_password

def worker(args):
    target_hash, algorithm, candidates = args
    for candidate in candidates:
        if hash_password(candidate, algorithm) == target_hash:
            return candidate
    return None

def brute_force(target_hash, algorithm, max_length=6, charset=None, threads=None):
    if charset is None:
        charset = string.ascii_lowercase + string.digits

    cores = multiprocessing.cpu_count()
    print(f"[*] Starting brute force attack...")
    print(f"[*] Charset: {charset}")
    print(f"[*] Max length: {max_length}")
    print(f"[*] CPU cores: {cores}")

    attempts = 0

    for length in range(1, max_length + 1):
        print(f"[*] Trying length {length}...")

        all_candidates = [''.join(c) for c in itertools.product(charset, repeat=length)]
        attempts += len(all_candidates)

        chunk_size = max(1, len(all_candidates) // cores)
        chunks = [all_candidates[i:i+chunk_size] for i in range(0, len(all_candidates), chunk_size)]
        tasks = [(target_hash, algorithm, chunk) for chunk in chunks]

        with multiprocessing.Pool(processes=cores) as pool:
            results = pool.map(worker, tasks)

        for result in results:
            if result:
                print(f"\n[+] PASSWORD FOUND!")
                print(f"[+] Password: {result}")
                print(f"[+] Attempts: {attempts:,}")
                return result

    print(f"[-] Password not found after {attempts:,} attempts.")
    return None